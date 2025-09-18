#!/usr/bin/env python3
"""
Quick script to display evaluation results from _results.jsonl files
"""
import sys
import json
import os

def show_results(results_file):
    """Display evaluation results"""
    
    if not os.path.exists(results_file):
        print(f"❌ Results file not found: {results_file}")
        return
    
    print(f"📊 Reading results from: {results_file}")
    print("=" * 60)
    
    try:
        with open(results_file, 'r') as f:
            results = [json.loads(line) for line in f]
        
        passed = sum(1 for r in results if r.get('passed', False))
        total = len(results)
        failed = total - passed
        pass_rate = passed / total if total > 0 else 0
        
        print(f"✅ Passed: {passed:,} problems")
        print(f"❌ Failed: {failed:,} problems")
        print(f"📊 Total:  {total:,} problems")
        print(f"🎯 Pass@1: {pass_rate:.6f} ({pass_rate:.2%})")
        print("=" * 60)
        print(f"{{'pass@1': {pass_rate}}}")
        
        # Show some failed examples if requested
        if len(sys.argv) > 2 and sys.argv[2] == "--show-failures":
            failed_tasks = [r for r in results if not r.get('passed', False)][:5]
            if failed_tasks:
                print(f"\n❌ First 5 failed tasks:")
                for i, task in enumerate(failed_tasks, 1):
                    print(f"  {i}. {task.get('task_id', 'Unknown')}")
        
    except Exception as e:
        print(f"❌ Error reading results: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python show_results.py <results_file.jsonl> [--show-failures]")
        print("Example: python show_results.py gpt-4o-mini_20-humaneval/mbpp_answers.jsonl_results.jsonl")
        sys.exit(1)
    
    results_file = sys.argv[1]
    show_results(results_file)
