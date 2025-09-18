# MBPP/689
### Completion
def min_jumps(arr, n):
    # If the array has less than 2 elements, no jumps are needed
    if n <= 1:
        return 0
    
    # Initialize variables
    jumps = 0          # Number of jumps made
    current_end = 0   # The farthest point we can reach with the current number of jumps
    farthest = 0      # The farthest point we can reach with the next jump
    
    for i in range(n - 1):  # We don't need to jump from the last element
        # Update the farthest point we can reach
        farthest = max(farthest, i + arr[i])
        
        # If we have reached the end of the current jump range
        if i == current_end:
            jumps += 1          # Increment the jump count
            current_end = farthest  # Update the current end to the farthest point
            
            # If the current end reaches or exceeds the last index, we can stop
            if current_end >= n - 1:
                break
    
    return jumps

# Test case
assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_jumps([1, 3, 6, 1, 0, 9], 6) == 3
    assert min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
    assert min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11) == 10
