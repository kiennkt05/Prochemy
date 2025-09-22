import os
import re
import json
import random
import subprocess
import concurrent.futures
import logging
import sys
from tqdm import tqdm
from evalplus.data import write_jsonl
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Set API Key
client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

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

# Generate task solution
def GEN_SOLUTION(task_describe, prompt, model_name="gpt-4o-mini"):
    global total_tokens_used
    attempts = 0
    while attempts < 3:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": task_describe},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.0
        )
        
        # Track token usage
        if hasattr(response, 'usage') and response.usage:
            total_tokens_used += response.usage.total_tokens
        
        # Use regex to match content starting with ```python and ending with ```
        match = re.search(r'```python(.*?)```', response.choices[0].message.content, re.DOTALL)
        if match:
            return response.choices[0].message.content, match.group(1).strip()  # Return the original response and the matched Python code part and strip extra whitespace
        attempts += 1

    # If no result after 3 attempts, return an empty string
    if logger:
        logger.warning(f"Failed to extract valid Python code after 3 attempts for prompt: {prompt}")
    return response.choices[0].message.content,""

# Process task
def process_task(task_id, task_describe, prompt, model_name="gpt-4o-mini"):
    response, completion = GEN_SOLUTION(task_describe, prompt, model_name)
    return dict(task_id=task_id, response=response, completion=completion)

# Read JSONL file
def read_jsonl(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

# Generate solutions and save to the specified directory
def generate_solutions(test_set_path, mutated_prompt_path, output_directory, model_name="gpt-4o-mini"):
    os.makedirs(output_directory, exist_ok=True)

    mutated_prompts = {task["prompt_id"]: task["mutated_prompt"] for task in read_jsonl(mutated_prompt_path)}

    for prompt_id, task_describe in mutated_prompts.items():
        samples = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [
                executor.submit(
                    process_task,
                    task["task_id"],
                    task_describe,
                    task["prompt"],
                    model_name
                )
                for task in read_jsonl(test_set_path)
            ]

            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures),
                               desc=f"Processing tasks for prompt_id {prompt_id}"):
                result = future.result()
                if result['completion']:
                    samples.append(result)
                else:
                    if logger:
                        logger.warning(f"No valid completion for task_id: {result['task_id']} with prompt_id: {prompt_id}")

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
                    # if logger:
                    #     logger.info(f"Generating results for {filename}...")
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

# Generate optimized prompts
def GEN_ANSWER(prompt, model_name="gpt-4o-mini"):
    global total_tokens_used
    response = client.chat.completions.create(
        model=model_name,
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
    parser.add_argument("--model", default="gpt-4o-mini", help="Model name to use for generation")
    parser.add_argument("--test_set_path", default="code_generation_training_set.jsonl", help="Path to test set")
    parser.add_argument("--mutated_prompt_path", default="mutated_prompts.jsonl", help="Path to mutated prompts")
    parser.add_argument("--output_directory", default="evaluation_results_auto", help="Output directory for results")
    parser.add_argument("--prompts_file_path", default="mutated_prompts.jsonl", help="Prompts file path")
    parser.add_argument("--best_prompt_output_path", default="best_prompt.jsonl", help="Best prompt output path")
    parser.add_argument("--optimize_output_file", default="optimized_prompts_auto.jsonl", help="Optimized prompts output")
    parser.add_argument("--max_iterations", type=int, default=10, help="Maximum number of iterations")
    parser.add_argument("--convergence_threshold", type=int, default=3, help="Convergence threshold")
    
    args = parser.parse_args()
    
    # Declare global variables
    global logger, total_tokens_used
    
    # Initialize token tracking
    total_tokens_used = 0
    
    model_safe_name = args.model.replace("/", "_").replace(":", "_")
    parent_folder = f"{model_safe_name}_{args.test_set_path.replace("/", "_").split(".")[0]}"
    os.makedirs(parent_folder, exist_ok=True)
    
    # Setup logging
    log_file_path = os.path.join(parent_folder, f"prochemy_pipeline_{args.test_set_path.replace("/", "_").split(".")[0]}.log")
    logger = setup_logging(log_file_path)
    
    logger.info("🧪 Starting Automated Prochemy Pipeline")
    logger.info(f"Model: {args.model}")
    logger.info(f"Parent folder: {parent_folder}")
    logger.info(f"Log file: {log_file_path}")
    logger.info(f"Max iterations: {args.max_iterations}")
    logger.info(f"Convergence threshold: {args.convergence_threshold}")
    logger.info("-" * 50)
    
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
        generate_solutions(test_set_path, prompts_file_path, iter_output_dir, args.model)
        
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
            optimize_prompts(iter_best_prompt, iter_optimize_output, args.model)
            
            # Update prompts_file_path for next iteration
            prompts_file_path = iter_optimize_output
    
    logger.info(f"\n✅ Pipeline completed!")
    logger.info(f"🏆 Best overall score: {best_overall_score:.3f}")
    logger.info(f"🔢 Total tokens used: {total_tokens_used:,}")
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