# MBPP/701
### Completion
def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        # Right sum is total_sum - left_sum - arr[i]
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]
    
    return -1  # Return -1 if no equilibrium index is found

# Test the function with the provided assertion
assert equilibrium_index([1, 2, 3, 4, 1, 2, 3]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert equilibrium_index([1, 2, 3, 4, 1, 2, 3]) == 3
    assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
    assert equilibrium_index([1, 2, 3]) == -1
