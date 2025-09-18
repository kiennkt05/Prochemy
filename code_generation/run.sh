cd D:/Documents/AI4SE/WorkSpace/Prochemy/code_generation
python prompt_test_humaneval_ET.py --model gpt-4o-mini --prompt_file alchemy/alchemy_optimized_prompt.jsonl  --dataset mbpp --output_path alchemy/alchemy_mbpp_answers.jsonl
evaluate_functional_correctness alchemy/alchemy_mbpp_answers.jsonl --problem_file Dataset/updated_mbpp_format.jsonl
python show_results.py alchemy/alchemy_mbpp_answers.jsonl_results.jsonl

cd D:/Documents/AI4SE/WorkSpace/Prochemy/code_generation
python prompt_test_humaneval_ET.py --model gpt-4o-mini --prompt_file alchemy/alchemy_optimized_prompt.jsonl  --dataset humaneval --output_path alchemy/alchemy_humaneval_answers.jsonl
evaluate_functional_correctness alchemy/alchemy_humaneval_answers.jsonl --problem_file Dataset/human-eval-v2-20210705.jsonl
python show_results.py alchemy/alchemy_humaneval_answers.jsonl_results.jsonl

cd D:/Documents/AI4SE/WorkSpace/Prochemy/code_generation
python 2+3+4_reinforcement.py --model gpt-4o --test_set_path code_generation_training_set.jsonl 
python prompt_test_humaneval_ET.py --model gpt-4o --prompt_file gpt-4o_code_generation_training_set/best_prompt.jsonl  --dataset mbpp --output_path gpt-4o_code_generation_training_set/gpt-4o_mbpp_answers.jsonl
evaluate_functional_correctness gpt-4o_code_generation_training_set/gpt-4o_mbpp_answers.jsonl --problem_file Dataset/updated_mbpp_format.jsonl
python show_results.py gpt-4o_code_generation_training_set/gpt-4o_mbpp_answers.jsonl_results.jsonl
python prompt_test_humaneval_ET.py --model gpt-4o --prompt_file origin_prompt.jsonl  --dataset mbpp --output_path gpt-4o_code_generation_training_set/gpt-4o-origin-prompt_mbpp_answers.jsonl
evaluate_functional_correctness gpt-4o_code_generation_training_set/gpt-4o-origin-prompt_mbpp_answers.jsonl --problem_file Dataset/updated_mbpp_format.jsonl
python show_results.py gpt-4o_code_generation_training_set/gpt-4o-origin-prompt_mbpp_answers.jsonl_results.jsonl