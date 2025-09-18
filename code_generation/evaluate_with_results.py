#!/usr/bin/env python3
"""
Wrapper script for evaluate_functional_correctness that always shows pass@1 results
"""
import sys
import os
import json
import subprocess
import argparse

def run_evaluation_and_show_results(sample_file, problem_file=None):
    """Run evaluation and always show the pass@1 results"""
    
    # Construct the command
    cmd = ["evaluate_functional_correctness", sample_file]
    if problem_file:
        cmd.extend(["--problem_file", problem_file])
    
    print(f"🚀 Running: {' '.join(cmd)}")
    print("-" * 60)
    
    # Run the evaluation
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("Stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"❌ Evaluation failed: {e}")
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
        return
    
    # Always read and display the results
    results_file = sample_file + "_results.jsonl"
    
    if os.path.exists(results_file):
        print("\n" + "=" * 60)
        print("📊 EVALUATION RESULTS")
        print("=" * 60)
        
        # Read and analyze results
        with open(results_file, 'r') as f:
            results = [json.loads(line) for line in f]
        
        passed = sum(1 for r in results if r.get('passed', False))
        total = len(results)
        pass_rate = passed / total if total > 0 else 0
        
        print(f"✅ Passed: {passed:,} / {total:,} problems")
        print(f"❌ Failed: {total - passed:,} problems")
        print(f"🎯 Pass@1: {pass_rate:.6f} ({pass_rate:.2%})")
        print(f"📁 Results saved to: {results_file}")
        print("=" * 60)
        
        # Also print in the format that evaluate_functional_correctness uses
        print(f"{{'pass@1': {pass_rate}}}")
        
    else:
        print(f"⚠️  Results file not found: {results_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run evaluate_functional_correctness and always show results")
    parser.add_argument("sample_file", help="Path to the sample file (generated solutions)")
    parser.add_argument("--problem_file", help="Path to the problem file")
    
    args = parser.parse_args()
    
    run_evaluation_and_show_results(args.sample_file, args.problem_file)
