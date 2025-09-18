# MBPP/60
### Completion
def max_len_sub(arr, diff):
    if not arr:
        return 0  # Return 0 for empty array
    
    max_length = 1  # At least one element can be a subsequence
    current_length = 1  # Start with the first element
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the absolute difference is equal to the given diff
        if abs(arr[i] - arr[i - 1]) == diff:
            current_length += 1  # Increase the current subsequence length
        else:
            # Update max_length if current_length is greater
            max_length = max(max_length, current_length)
            current_length = 1  # Reset current_length for a new subsequence
    
    # Final check to update max_length after the loop
    max_length = max(max_length, current_length)
    
    return max_length

# Test case
assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_len_sub([2, 5, 6, 3, 7, 6, 5, 8], 8) == 5
    assert max_len_sub([-2, -1, 5, -1, 4, 0, 3], 7) == 4
    assert max_len_sub([9, 11, 13, 15, 18], 5) == 1
