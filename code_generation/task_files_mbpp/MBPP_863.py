# MBPP/863
### Completion
def find_longest_conseq_subseq(arr, n):
    if n == 0:
        return 0
    
    # Create a set from the array to get unique elements
    unique_elements = set(arr)
    longest_streak = 0
    
    for num in unique_elements:
        # Check if it's the start of a sequence
        if num - 1 not in unique_elements:
            current_num = num
            current_streak = 1
            
            # Count the length of the consecutive sequence
            while current_num + 1 in unique_elements:
                current_num += 1
                current_streak += 1
            
            # Update the longest streak found
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

# Test the function with the provided assertion
assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_longest_conseq_subseq([1, 2, 2, 3], 4) == 3
    assert find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7) == 4
    assert find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5
