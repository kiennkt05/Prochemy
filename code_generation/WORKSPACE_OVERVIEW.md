# 🧪 Prochemy Workspace Overview

## 🎯 Main Focus: `gpt-4o-mini_code_generation_training_set/`
**This is your primary results folder with the interactive visualization!**

### Key Files:
- `visualize.html` - **Interactive dashboard** (click bars to view details)
- `weighted_scores_analysis_correct.json` - Analysis data
- `prochemy_pipeline_*.log` - Pipeline execution logs
- `evaluation_results_auto_iter_*/` - Detailed results by iteration

## 🚀 Quick Actions:

### View Results
```bash
# Open the main visualization
open gpt-4o-mini_code_generation_training_set/visualize.html
```

### Run Pipeline
```bash
# Run the main optimization pipeline
python 2+3+4_reinforcement.py
```

### Check Specific Results
```bash
# View results for any file
python show_results.py <path_to_results_file>
```

## 📊 Current Status:
- **Best Score**: 254.56 (Iteration 3, Prompt 4)
- **Dataset**: 15 tasks, 5 iterations, 39 prompts
- **Visualization**: Fully interactive with click functionality

## 🗂️ Other Folders:
- `Dataset/` - Original datasets
- `gpt-4o-mini_20-*/` - Other experiment results
- `evalplus/` - Evaluation framework
- `human_eval/` - HumanEval evaluation tools

## 🧹 Cleanup Complete:
- Removed 15+ temporary files
- Consolidated duplicate datasets
- Organized main results in one folder
- Added clear documentation
