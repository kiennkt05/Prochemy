# Prochemy Code Generation Workspace

This workspace contains the Prochemy pipeline for automated prompt optimization in code generation tasks.

## 📁 Main Structure

### Core Pipeline Files
- `0_train_set_generate.py` - Generate training datasets
- `0_train_set_select.py` - Select training data
- `1_prompt_mutate.py` - Mutate prompts for optimization
- `2_prompt_evaluate.py` - Evaluate prompt performance
- `2+3+4_reinforcement.py` - Main reinforcement learning pipeline
- `3_cal_pass1_score_and_select_best_prompt.py` - Calculate scores and select best prompts
- `3_reinforcement_cal_score_and_select.py` - Reinforcement learning score calculation

### Evaluation Tools
- `evaluate_with_results.py` - Evaluate results with existing data
- `show_results.py` - Display evaluation results
- `post_processing.py` - Post-process evaluation results
- `post_processing_modified.py` - Modified post-processing

### Dataset Folders
- `Dataset/` - Original datasets (HumanEval, MBPP)
- `gpt-4o-mini_code_generation_training_set/` - **Main results folder** with visualization
- `gpt-4o-mini_20-humaneval/` - HumanEval evaluation results
- `gpt-4o-mini_20-mbpp/` - MBPP evaluation results
- `gpt-4o-mini_20-mbpp-x/` - Extended MBPP results
- `o4-mini/` - O4-mini model results
- `o4-mini_1/` - O4-mini variant results

### Visualization
- `gpt-4o-mini_code_generation_training_set/visualize.html` - **Interactive visualization dashboard**
- `gpt-4o-mini_code_generation_training_set/weighted_scores_analysis_correct.json` - Analysis data

## 🎯 Key Features

### Interactive Visualization
The main visualization (`gpt-4o-mini_code_generation_training_set/visualize.html`) provides:
- **Clickable Charts**: Click any bar in the main chart to view detailed breakdown
- **Dropdown Selection**: Choose iteration and prompt from dropdowns
- **Weighted Score Analysis**: View task-by-task weighted scores
- **Missing Prompt Handling**: Shows empty charts for failed prompts

### Weighted Scoring System
- Tasks solved by fewer prompts receive higher weights
- Weight = total_correct_solutions / task_correct_count
- Higher weights indicate more difficult tasks

## 🚀 Quick Start

1. **View Results**: Open `gpt-4o-mini_code_generation_training_set/visualize.html` in browser
2. **Run Pipeline**: Execute `python 2+3+4_reinforcement.py` for new optimization
3. **Check Results**: Use `python show_results.py <results_file>` to view specific results

## 📊 Current Best Results

- **Best Overall Score**: 254.56 (Iteration 3, Prompt 4)
- **Dataset**: gpt-4o-mini_code_generation_training_set
- **Tasks**: 15 (mix of HumanEval and auto-generated)
- **Total Prompts**: 39 available across 5 iterations

## 🧹 Cleanup Notes

Temporary analysis files have been removed to keep the workspace clean:
- Analysis scripts (completed tasks)
- Debug files (no longer needed)
- Duplicate data files (consolidated)
- Test files (functionality verified)
