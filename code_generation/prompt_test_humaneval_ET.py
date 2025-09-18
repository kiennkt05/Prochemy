import re
import json
import os
from evalplus.data import write_jsonl
from openai import OpenAI
import concurrent.futures
from tqdm import tqdm
from dotenv import load_dotenv


load_dotenv()

# Set the API key
client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# TODO: change the prompt - this will be loaded from the prompt file
task_describe_template = ""


def GEN_SOLUTION(prompt, entry_point, model_name="gpt-4o-mini"):
    attempts = 0
    task_describe = task_describe_template.format(entry_point=entry_point)

    while attempts < 5:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": task_describe},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.0
        )
        # Use regular expression to match content starting with ```python and ending with ```
        match = re.search(r'```python(.*?)```', response.choices[0].message.content, re.DOTALL)
        if match:
            code = match.group(1).strip()
            # More flexible function name validation - check if any function is defined
            # This handles cases where the model corrects typos in function names
            func_match = re.search(r'def\s+(\w+)\s*\(', code)
            if func_match or entry_point in code:
                return code
        attempts += 1

    # If no result after 5 attempts, print a message and return None
    print(f"Failed to extract valid Python code after 5 attempts for prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}")
    # Return the raw response
    return response.choices[0].message.content


def process_task(task_id, prompt, entry_point, model_name="gpt-4o-mini"):
    completion = GEN_SOLUTION(prompt, entry_point, model_name)
    return dict(task_id=task_id, entry_point=entry_point, completion=completion)

def load_tasks_from_jsonl(file_path):
    tasks = {}
    with open(file_path, 'r') as file:
        for line in file:
            task = json.loads(line)
            tasks[task['task_id']] = task
    return tasks


def load_prompt_from_file(prompt_file_path):
    """Load prompt from JSONL file (takes the first prompt)"""
    with open(prompt_file_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line:
            prompt_data = json.loads(first_line)
            return prompt_data.get('mutated_prompt', '')
    return ""

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test prompts on HumanEval/MBPP datasets")
    parser.add_argument("--model", default="gpt-4o-mini", help="Model name to use for generation")
    parser.add_argument("--prompt_file", required=True, help="Path to prompt JSONL file")
    parser.add_argument("--dataset", default="humaneval", choices=["humaneval", "mbpp"], help="Dataset to test on")
    parser.add_argument("--dataset_path", help="Custom dataset path (optional)")
    parser.add_argument("--output_path", required=True, help="Output file path")
    parser.add_argument("--max_problems", type=int, help="Maximum number of problems to test (optional)")
    parser.add_argument("--max_workers", type=int, default=10, help="Number of worker threads")
    
    args = parser.parse_args()
    
    # Load prompt from file
    task_describe_template = load_prompt_from_file(args.prompt_file)
    print(f"🤖 Using model: {args.model}")
    print(f"📝 Loaded prompt from: {args.prompt_file}")
    print(f"📏 Prompt length: {len(task_describe_template)} characters")
    
    # Determine dataset path
    if args.dataset_path:
        input_file_path = args.dataset_path
    elif args.dataset == "humaneval":
        input_file_path = "Dataset/human-eval-v2-20210705.jsonl"
    elif args.dataset == "mbpp":
        input_file_path = "Dataset/updated_mbpp_format.jsonl"
    else:
        raise ValueError(f"Unknown dataset: {args.dataset}")
    
    print(f"📊 Loading dataset: {input_file_path}")
    problems = load_tasks_from_jsonl(input_file_path)
    
    # Limit problems if specified
    if args.max_problems:
        problems = dict(list(problems.items())[:args.max_problems])
        print(f"🔢 Limited to {len(problems)} problems")
    
    print(f"🚀 Processing {len(problems)} problems with {args.max_workers} workers...")
    
    samples = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = [
            executor.submit(process_task, task_id, problem["prompt"], problem["entry_point"], args.model)
            for task_id, problem in problems.items()
        ]

        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing tasks"):
            samples.append(future.result())

    print(f"💾 Saving results to: {args.output_path}")
    write_jsonl(args.output_path, samples)
    print(f"✅ Completed! Generated {len(samples)} solutions.")