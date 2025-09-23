import os
import re
import json
import random
import subprocess
import concurrent.futures
import logging
import sys
from accelerate.utils import gather_object
from accelerate import PartialState
from tqdm import tqdm
from evalplus.data import write_jsonl
from openai import OpenAI
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Global variables for HF model
hf_model = None
hf_tokenizer = None
device = None

def initialize_hf_model(model_name):
    """Initialize Hugging Face model and tokenizer"""
    global hf_model, hf_tokenizer, device
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")
    
    try:
        # Load tokenizer
        hf_tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        
        # Need to set the padding token to the eos token for generation
        if hf_tokenizer.eos_token:
            hf_tokenizer.pad_token = hf_tokenizer.eos_token
        else:
            hf_tokenizer.add_special_tokens({
                "pad_token": "<pad>"
            })
        
        # Load model
        hf_model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
            trust_remote_code=True
        )
        
        if not torch.cuda.is_available():
            hf_model = hf_model.to(device)
            
        hf_model.eval()
        logger.info(f"Successfully loaded model: {model_name}")
        
    except Exception as e:
        logger.error(f"Failed to load model {model_name}: {e}")
        raise

def generate_with_hf_model(system_prompt, user_prompt, max_tokens=1000, temperature=0.0):
    """Generate response using Hugging Face model"""
    global hf_model, hf_tokenizer, device
    
    # Format the prompt for Qwen models
    # Qwen models typically use a chat format
    if "qwen" in hf_tokenizer.name_or_path.lower():
        # Use Qwen's chat template if available
        if hasattr(hf_tokenizer, 'apply_chat_template'):
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            formatted_prompt = hf_tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
        else:
            # Fallback formatting for Qwen
            formatted_prompt = f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{user_prompt}<|im_end|>\n<|im_start|>assistant\n"
    else:
        # Generic format
        formatted_prompt = f"System: {system_prompt}\n\nUser: {user_prompt}\n\nAssistant:"
    
    # Tokenize input
    inputs = hf_tokenizer(
        formatted_prompt, 
        return_tensors="pt", 
        truncation=True, 
        max_length=2048  # Adjust based on model's context length
    ).to(device)
    
    # Generate response
    with torch.no_grad():
        outputs = hf_model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature if temperature > 0 else 0.1,  # Avoid 0 temperature
            do_sample=temperature > 0,
            pad_token_id=hf_tokenizer.pad_token_id,
            eos_token_id=hf_tokenizer.eos_token_id,
            repetition_penalty=1.1,
            top_p=0.9 if temperature > 0 else None
        )
    
    # Decode response
    response = hf_tokenizer.decode(
        outputs[0][inputs['input_ids'].shape[1]:], 
        skip_special_tokens=True
    ).strip()
    
    return response

def generate_batch_with_chat_template(system_prompt, user_prompts, max_tokens=2048, temperature=0.0):
    """Generate responses using Hugging Face model with chat templates for batching"""
    global hf_model, hf_tokenizer, device
    
    # Prepare messages for each user prompt
    batch_messages = []
    for user_prompt in user_prompts:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        batch_messages.append(messages)
    
    # Format prompts using chat template
    formatted_prompts = []
    for messages in batch_messages:
        if "qwen" in hf_tokenizer.name_or_path.lower():
            # Use Qwen's chat template if available
            if hasattr(hf_tokenizer, 'apply_chat_template'):
                formatted_prompt = hf_tokenizer.apply_chat_template(
                    messages, 
                    tokenize=False, 
                    add_generation_prompt=True
                )
            else:
                # Fallback formatting for Qwen
                formatted_prompt = f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{messages[1]['content']}<|im_end|>\n<|im_start|>assistant\n"
        else:
            # Generic format
            formatted_prompt = f"System: {system_prompt}\n\nUser: {messages[1]['content']}\n\nAssistant:"
        
        formatted_prompts.append(formatted_prompt)
    
    # Tokenize all prompts in the batch
    padding_side_default = hf_tokenizer.padding_side
    hf_tokenizer.padding_side = "left"
    
    inputs = hf_tokenizer(
        formatted_prompts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=4096,  # Adjust based on model's context length
        return_token_type_ids=False
    ).to(device)
    
    # Restore original padding side
    hf_tokenizer.padding_side = padding_side_default
    
    # Generate responses
    with torch.no_grad():
        outputs = hf_model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature if temperature > 0 else 0.1,
            do_sample=temperature > 0,
            pad_token_id=hf_tokenizer.pad_token_id,
            eos_token_id=hf_tokenizer.eos_token_id,
            repetition_penalty=1.1,
            top_p=0.9 if temperature > 0 else None,
            num_beams=1
        )
    
    # Decode responses
    prompt_len = inputs['input_ids'].shape[1]
    responses = []
    for i in range(outputs.shape[0]):
        response = hf_tokenizer.decode(
            outputs[i][prompt_len:], 
            skip_special_tokens=True
        ).strip()
        responses.append(response)
    
    return responses

# Setup logging configuration
def setup_logging(log_file_path):
    """Setup logging to both console and file"""
    # Create logger
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    
    # Clear existing handlers
    for handler in log.handlers[:]:
        log.removeHandler(handler)
    
    # Disable HTTP request logging
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    
    # Create formatter
    formatter = logging.Formatter('%(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
    
    return log

# Global logger instance will be initialized in main
# Global token usage tracking will be initialized in main

# Task description and information used for generating optimized prompts
task_describe = """
You are an expert prompt engineer.
"""

information = """
Please help me improve the given prompt to get a more helpful and harmless response.
Suppose I need to generate a Python program based on natural language descriptions.
The generated Python program should be able to complete the tasks described in natural language and pass any test cases specific to those tasks.\n
"""

format = """
You may add any information you think will help improve the task's effectiveness during the prompt optimization process.
If you find certain expressions and wording in the original prompt inappropriate, you can also modify these usages.
Ensure that the optimized prompt includes a detailed task description and clear process guidance added to the original prompt.
Wrap the optimized prompt in {{}}.
"""

# Generate task solution using HF model
def GEN_SOLUTION(task_describe, prompt, model_name="Qwen/Qwen2.5-Coder-7B-Instruct"):
    global total_tokens_used, hf_model, hf_tokenizer
    
    attempts = 0
    while attempts < 3:
        try:
            # Generate response using HF model with chat template
            response_content = generate_batch_with_chat_template(
                system_prompt=task_describe,
                user_prompts=[prompt],
                max_tokens=2048,
                temperature=0.0
            )[0]  # Get first (and only) response from batch
            
            # Estimate token usage (approximate)
            estimated_tokens = len(hf_tokenizer.encode(prompt + response_content))
            total_tokens_used += estimated_tokens
            
            # Use regex to match content starting with ```python and ending with ```
            match = re.search(r'```python(.*?)```', response_content, re.DOTALL)
            if match:
                return response_content, match.group(1).strip()
            
            attempts += 1
            
        except Exception as e:
            logger.error(f"Error generating solution: {e}")
            attempts += 1
            if attempts >= 3:
                break

    # If no result after 3 attempts, return an empty string
    if logger:
        logger.warning(f"Failed to extract valid Python code after 3 attempts for prompt: {prompt}")
    return response_content if 'response_content' in locals() else "", ""

# Process task
def process_task(task_id, task_describe, prompt, model_name="Qwen/Qwen2.5-Coder-7B-Instruct"):
    response, completion = GEN_SOLUTION(task_describe, prompt, model_name)
    return dict(task_id=task_id, response=response, completion=completion)

# Read JSONL file
def read_jsonl(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

# Generate solutions and save to the specified directory
def generate_solutions(test_set_path, mutated_prompt_path, output_directory, model_name="Qwen/Qwen2.5-Coder-7B-Instruct", batch_size=8):
    os.makedirs(output_directory, exist_ok=True)

    mutated_prompts = {task["prompt_id"]: task["mutated_prompt"] for task in read_jsonl(mutated_prompt_path)}
    tasks = list(read_jsonl(test_set_path))  # Keep full task objects

    for prompt_id, system_prompt in mutated_prompts.items():
        # Create batched tasks with system and user prompts separated
        batched_user_prompts = []
        for i in range(0, len(tasks), batch_size):
            batch = tasks[i:i+batch_size]
            # Extract user prompts for this batch
            user_prompts = [task['prompt'] for task in batch]
            batched_user_prompts.append(user_prompts)
    
        completions_per_process = []
        distributed_state = PartialState()
        with distributed_state.split_between_processes(batched_user_prompts, apply_padding=False) as user_prompt_batches:
            for user_prompts in tqdm(user_prompt_batches, desc=f"Generating completions for prompt: {prompt_id}"):
                # Generate responses using chat template
                batch_responses = generate_batch_with_chat_template(
                    system_prompt=system_prompt,
                    user_prompts=user_prompts,
                    max_tokens=2048,
                    temperature=0.0
                )
                completions_per_process.extend(batch_responses)
        
        completions_gather = gather_object(completions_per_process)
        
        # Drop duplicates produced by apply_padding in split_between_processes
        responses = completions_gather[: len(tasks)]
        completions = []
        for response in responses:
            match = re.search(r'```python(.*?)```', response, re.DOTALL)
            if match:
                completions.append(match.group(1).strip())
            else:
                completions.append("")
        
        samples = [dict(task_id=task["task_id"], response=response, completion=completion) for task, response, completion in zip(tasks, responses, completions)]
        if distributed_state.is_main_process:
            # Train set name
            output_file = os.path.join(output_directory, f"train_set_{model_name.replace('/', '_')}_{prompt_id}.jsonl")
            write_jsonl(output_file, samples)

# Evaluate the generated solutions and select the best prompts
def evaluate_and_select_best_prompts(folder_path, problem_file_path, prompts_file_path, best_prompt_output_path):
    base_command = f"evaluate_functional_correctness {{jsonl_file}} --problem_file={problem_file_path}"

    # Used to store the correct result count for each task_id
    total_prompts = 0
    task_correct_counts = {}
    max_weighted_score = -1
    best_prompt_ids = []

    # Iterate over all jsonl files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jsonl") and not filename.endswith("_results.jsonl"):
            jsonl_file_path = os.path.join(folder_path, filename)
            result_file_path = jsonl_file_path + "_results.jsonl"

            # Check if results.jsonl file exists, if not, run the script to generate it
            if not os.path.exists(result_file_path):
                command = base_command.format(jsonl_file=jsonl_file_path)
                try:
                    if logger:
                        logger.info(f"Generating results for {filename}...")
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    if logger:
                        logger.error(f"Command failed: {e}\n{e.output}")
                    continue  # Skip this file if generation fails

            # Read the generated results.jsonl file and calculate correct counts for each task_id
            if os.path.exists(result_file_path):
                # Only count the prompts that have results
                total_prompts += 1
                with open(result_file_path, 'r') as result_file:
                    for line in result_file:
                        line = line.strip()  # Strip trailing whitespace
                        if not line:
                            if logger:
                                logger.warning(f"Warning: Empty line encountered in {result_file_path}")
                            continue  # Skip empty lines

                        try:
                            result_data = json.loads(line)
                        except json.JSONDecodeError as e:
                            if logger:
                                logger.error(f"Error decoding JSON in file {result_file_path}, line content: {line}")
                            continue  # Skip lines with JSON decoding errors

                        task_id = result_data.get('task_id')
                        if result_data.get('passed'):
                            task_correct_counts[task_id] = task_correct_counts.get(task_id, 0) + 1

    # Calculate weighted score for each task_id
    # total_tasks = sum(task_correct_counts.values())
    task_weights = {task_id: total_prompts / count for task_id, count in task_correct_counts.items()}
    
    # logger.info(f"Task weights: {task_weights}")

    # Recalculate weighted score and original score for each file
    prompt_scores = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".jsonl") and not filename.endswith("_results.jsonl"):
            jsonl_file_path = os.path.join(folder_path, filename)
            result_file_path = jsonl_file_path + "_results.jsonl"

            weighted_score = 0
            total_count = 0
            passed_count = 0

            if os.path.exists(result_file_path):
                with open(result_file_path, 'r') as result_file:
                    for line in result_file:
                        line = line.strip()  # Strip trailing whitespace
                        if not line:
                            if logger:
                                logger.warning(f"Warning: Empty line encountered in {result_file_path}")
                            continue  # Skip empty lines

                        try:
                            result_data = json.loads(line)
                        except json.JSONDecodeError as e:
                            if logger:
                                logger.error(f"Error decoding JSON in file {result_file_path}, line content: {line}")
                            continue  # Skip lines with JSON decoding errors

                        task_id = result_data.get('task_id')
                        total_count += 1
                        if result_data.get('passed'):
                            passed_count += 1
                            weighted_score += task_weights.get(task_id, 0)

            original_score = passed_count / total_count if total_count > 0 else 0

            # Extract prompt_id from filename
            try:
                prompt_id = int(re.search(r'_(\d+)\.jsonl', filename).group(1))
            except (IndexError, ValueError, AttributeError):
                if logger:
                    logger.error(f"Error extracting prompt_id from filename: {filename}")
                continue  # Skip this file

            prompt_scores[prompt_id] = {'original_score': original_score, 'weighted_score': weighted_score}

            # Update highest weighted score and corresponding prompt_id list
            if weighted_score > max_weighted_score:
                max_weighted_score = weighted_score
                best_prompt_ids = [prompt_id]  # Reset the list
            elif weighted_score == max_weighted_score:
                best_prompt_ids.append(prompt_id)

    # Print the original and weighted scores for each prompt_id
    for prompt_id, scores in prompt_scores.items():
        if logger:
            logger.info(
                f"Prompt ID: {prompt_id}, Original Score: {scores['original_score']}, Weighted Score: {scores['weighted_score']}")

    # Extract the corresponding prompt from the mutated_prompt file and save
    if best_prompt_ids:
        with open(prompts_file_path, 'r') as prompts_file:
            with open(best_prompt_output_path, 'w') as best_prompt_file:
                for line in prompts_file:
                    prompt_data = json.loads(line)
                    if prompt_data.get('prompt_id') in best_prompt_ids:
                        best_prompt_file.write(json.dumps(prompt_data) + '\n')

    if logger:
        logger.info(
            f'Best prompts saved to {best_prompt_output_path} with prompt_ids: {best_prompt_ids} and max weighted score: {max_weighted_score}')
    
    return max_weighted_score

# Generate optimized prompts (still using OpenAI for prompt optimization)
def GEN_ANSWER(prompt, model_name="gpt-4o-mini"):
    global total_tokens_used
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Fix gpt-4o-mini for mutating prompts
        messages=[
            {"role": "system", "content": task_describe},
            {"role": "user", "content": information + prompt + format}
        ],
        max_tokens=500,
        temperature=1.0
    )
    
    # Track token usage
    if hasattr(response, 'usage') and response.usage:
        total_tokens_used += response.usage.total_tokens
    
    return response.choices[0].message.content

def extract_wrapped_content(text):
    match = re.search(r'\{\{(.*?)\}\}', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return ""

def process_optimization_task(task_id, prompt, model_name="gpt-4o-mini"):
    while True:
        completion = GEN_ANSWER(prompt, model_name)
        wrapped_content = extract_wrapped_content(completion)
        if wrapped_content:
            return dict(prompt_id=task_id, mutated_prompt=wrapped_content)
        else:
            if logger:
                logger.warning(f"Task {task_id}: No wrapped content found. Retrying...")

def generate_new_prompts(existing_prompts, model_name="gpt-4o-mini"):
    new_prompts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for task_id in range(10):
            random_prompt = random.choice(existing_prompts)
            prompt_text = random_prompt['mutated_prompt']
            formatted_prompt = f"The prompt ready to be optimized are as follows and wrapped in []:\n[{prompt_text}]\n"
            futures.append(executor.submit(process_optimization_task, task_id, formatted_prompt, model_name))

        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing tasks"):
            new_prompts.append(future.result())

    return new_prompts

def optimize_prompts(input_file, output_file, model_name="gpt-4o-mini"):
    if not os.path.exists(input_file):
        if logger:
            logger.error(f"Input file {input_file} does not exist.")
        return

    with open(input_file, 'r') as file:
        prompts = [json.loads(line) for line in file]

    new_prompts = generate_new_prompts(prompts, model_name)

    existing_ids = {prompt['prompt_id'] for prompt in prompts}
    new_id = 0
    for new_prompt in new_prompts:
        while new_id in existing_ids:
            new_id += 1
        new_prompt['prompt_id'] = new_id
        existing_ids.add(new_id)

    new_prompts = [prompt for prompt in new_prompts if prompt['prompt_id'] <= 9]

    combined_prompts = prompts + new_prompts
    with open(output_file, 'w') as out_file:
        for prompt in combined_prompts:
            json.dump(prompt, out_file)
            out_file.write('\n')

    if logger:
        logger.info(f"New prompts saved to {output_file}")

# Main program entry point
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Automated Prochemy Reinforcement Learning Pipeline")
    parser.add_argument("--model_name", default="Qwen/Qwen2.5-Coder-7B-Instruct", help="HuggingFace model name to use for generation")
    parser.add_argument("--test_set_path", default="code_generation_training_set.jsonl", help="Path to test set")
    parser.add_argument("--mutated_prompt_path", default="mutated_prompts.jsonl", help="Path to mutated prompts")
    parser.add_argument("--output_directory", default="evaluation_results_auto", help="Output directory for results")
    parser.add_argument("--prompts_file_path", default="mutated_prompts.jsonl", help="Prompts file path")
    parser.add_argument("--best_prompt_output_path", default="best_prompt.jsonl", help="Best prompt output path")
    parser.add_argument("--optimize_output_file", default="optimized_prompts_auto.jsonl", help="Optimized prompts output")
    parser.add_argument("--max_iterations", type=int, default=10, help="Maximum number of iterations")
    parser.add_argument("--convergence_threshold", type=int, default=3, help="Convergence threshold")
    parser.add_argument("--batch_size", type=int, default=8, help="Batch size")
    
    args = parser.parse_args()
    
    # Declare global variables
    global logger, total_tokens_used
    
    # Initialize token tracking
    total_tokens_used = 0
    
    model_safe_name = args.model_name.replace('/', '_').replace(":", '_')
    parent_folder = f"{model_safe_name}_{args.test_set_path.replace('/', '_').split('.')[0]}"
    os.makedirs(parent_folder, exist_ok=True)
    
    # Setup logging
    log_file_path = os.path.join(parent_folder, f"prochemy_pipeline_{args.test_set_path.replace('/', '_').split('.')[0]}.log")
    logger = setup_logging(log_file_path)
    
    logger.info("🧪 Starting Automated Prochemy Pipeline with HuggingFace Models")
    logger.info(f"Model: {args.model_name}")
    logger.info(f"Parent folder: {parent_folder}")
    logger.info(f"Log file: {log_file_path}")
    logger.info(f"Max iterations: {args.max_iterations}")
    logger.info(f"Convergence threshold: {args.convergence_threshold}")
    logger.info("-" * 50)
    
    # Initialize HuggingFace model
    logger.info(f"🤗 Initializing HuggingFace model: {args.model_name}")
    try:
        initialize_hf_model(args.model_name)
    except Exception as e:
        logger.error(f"Failed to initialize model: {e}")
        sys.exit(1)
    
    # Track best score across iterations
    best_overall_score = 0.0
    best_iteration = 0
    best_prompt = ""
    best_prompt_data = None  # Initialize to avoid undefined variable error
    no_improvement_count = 0
    
    # Use the provided parameters and update paths to use parent folder
    test_set_path = args.test_set_path
    # mutated_prompt_path = os.path.join(parent_folder, args.mutated_prompt_path)
    output_directory = os.path.join(parent_folder, args.output_directory)
    problem_file_path = args.test_set_path
    prompts_file_path = os.path.join(parent_folder, args.prompts_file_path)
    best_prompt_output_path = os.path.join(parent_folder, args.best_prompt_output_path)
    optimize_output_file = os.path.join(parent_folder, args.optimize_output_file)
    
    # Create necessary directories
    os.makedirs(os.path.join(parent_folder, "best_prompt"), exist_ok=True)
    os.makedirs(os.path.join(parent_folder, "optimized_prompts"), exist_ok=True)
    
    # Copy initial files to parent folder if they don't exist there
    if not os.path.exists(prompts_file_path) and os.path.exists(args.mutated_prompt_path):
        import shutil
        shutil.copy2(args.mutated_prompt_path, prompts_file_path)
        logger.info(f"📋 Copied {args.mutated_prompt_path} to {prompts_file_path}")
    
    for iteration in range(1, args.max_iterations + 1):
        logger.info(f"\n🔄 Iteration {iteration}/{args.max_iterations}")
        logger.info("=" * 50)
        
        # Create iteration-specific output directory
        iter_output_dir = os.path.join(output_directory, f"iter_{iteration}")
        os.makedirs(iter_output_dir, exist_ok=True)  # Optional safety check

        # Generate solutions
        logger.info("📝 Generating solutions...")
        generate_solutions(test_set_path, prompts_file_path, iter_output_dir, args.model_name, args.batch_size)
        
        # Evaluate solutions and select the best prompts
        logger.info("📊 Evaluating and selecting best prompts...")
        folder_path = iter_output_dir
        iter_best_prompt = os.path.join(parent_folder, "best_prompt", f"iter_{iteration}.jsonl")
        current_score = evaluate_and_select_best_prompts(folder_path, problem_file_path, prompts_file_path, iter_best_prompt)
        
        logger.info(f"📈 Current iteration score: {current_score:.3f}")
        
        # Check for improvement
        if current_score > best_overall_score:
            best_overall_score = current_score
            best_iteration = iteration
            # Store the best prompt by reading from the best prompt file
            if os.path.exists(iter_best_prompt):
                try:
                    with open(iter_best_prompt, 'r') as f:
                        best_prompt_data = []
                        for line in f:
                            best_prompt_data.append(json.loads(line.strip()))
                        if best_prompt_data:
                            # Store the first (best) prompt's content
                            best_prompt = best_prompt_data[0].get('mutated_prompt', '')
                except Exception as e:
                    if logger:
                        logger.warning(f"Could not read best prompt from {iter_best_prompt}: {e}")
            no_improvement_count = 0
            logger.info(f"🎉 New best score achieved: {best_overall_score:.3f}")
        else:
            no_improvement_count += 1
            logger.info(f"📉 No improvement for {no_improvement_count} iteration(s)")
        
        # Check convergence
        if no_improvement_count >= args.convergence_threshold:
            break
        
        # Generate optimized prompts for next iteration (if not the last iteration)
        if iteration < args.max_iterations:
            logger.info("🔄 Generating optimized prompts for next iteration...")
            iter_optimize_output = os.path.join(parent_folder, "optimized_prompts", f"iter_{iteration}.jsonl")
            optimize_prompts(iter_best_prompt, iter_optimize_output, args.model_name)
            
            # Update prompts_file_path for next iteration
            prompts_file_path = iter_optimize_output
    
    logger.info(f"\n✅ Pipeline completed!")
    logger.info(f"🏆 Best overall score: {best_overall_score:.3f}")
    logger.info(f"🔢 Total tokens used (estimated): {total_tokens_used:,}")
    logger.info(f"📁 All results saved in: {parent_folder}")

    # Save the best prompt
    if best_prompt_data is not None:
        best_prompt_path = os.path.join(parent_folder, "best_prompt", "best_prompt.jsonl")
        with open(best_prompt_path, 'w') as f:
            json.dump(best_prompt_data[0], f)
        logger.info(f"📁 Best prompts saved in: {best_prompt_path}")
    else:
        logger.warning("⚠️  No best prompt data to save")
    
    
    # Log the best prompt content
    if best_prompt:
        logger.info(f"\n🌟 Best Prompt (from iteration {best_iteration}):")
        logger.info("-" * 80)
        logger.info(best_prompt)
        logger.info("-" * 80)
    else:
        logger.info(f"\n⚠️  Best prompt content could not be retrieved")
    
    # Clean up GPU memory
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    logger.info("🧹 Cleaned up GPU memory")