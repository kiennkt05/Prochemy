# MBPP/476
### Completion
def big_sum(arr):
    """
    Calculate the sum of the largest and smallest values in the given array.

    Parameters:
    arr (list): A list of numerical values.

    Returns:
    int/float: The sum of the largest and smallest values in the array.
    """
    if not arr:  # Check if the array is empty
        raise ValueError("The array should not be empty.")
    
    largest = max(arr)  # Find the largest value
    smallest = min(arr)  # Find the smallest value
    
    return largest + smallest  # Return the sum of largest and smallest

# Test case
assert big_sum([1, 2, 3]) == 4  # 1 (smallest) + 3 (largest) = 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert big_sum([1,2,3]) == 4
    assert big_sum([-1,2,3,4]) == 3
    assert big_sum([2,3,6]) == 8
