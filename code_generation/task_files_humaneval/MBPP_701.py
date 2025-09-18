# MBPP/701
### Completion
def equilibrium_index(arr):
    total_sum = sum(arr)  # Calculate the total sum of the array
    left_sum = 0  # Initialize left sum to 0
    
    for i in range(len(arr)):
        # Right sum is total_sum - left_sum - arr[i]
        right_sum = total_sum - left_sum - arr[i]
        
        # Check if left sum equals right sum
        if left_sum == right_sum:
            return i  # Return the equilibrium index
        
        # Update left sum for the next iteration
        left_sum += arr[i]
    
    return -1  # Return -1 if no equilibrium index is found

# Test case
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
