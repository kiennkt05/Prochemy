# MBPP/149
### Completion
def longest_subseq_with_diff_one(arr, n):
    if n == 0:
        return 0
    
    # Dictionary to store the length of longest subsequence ending with each number
    length_map = {}
    
    # Initialize the maximum length
    max_length = 1
    
    for num in arr:
        # Length of subsequence ending with num
        current_length = 1
        
        # Check for num - 1
        if num - 1 in length_map:
            current_length = length_map[num - 1] + 1
        
        # Check for num + 1
        if num + 1 in length_map:
            current_length = max(current_length, length_map[num + 1] + 1)
        
        # Update the length_map for the current number
        length_map[num] = current_length
        
        # Update the maximum length found
        max_length = max(max_length, current_length)
    
    return max_length

# Test case
assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
    assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
    assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7
