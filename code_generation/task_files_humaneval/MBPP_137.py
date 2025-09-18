# MBPP/137
### Completion
def zero_count(arr):
    """
    Calculate the ratio of zeroes in the given array of integers.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    float: The ratio of zeroes in the array. Returns 0.0 if the array is empty.
    """
    if not arr:  # Check if the array is empty
        return 0.0
    
    zeroes = arr.count(0)  # Count the number of zeroes in the array
    total_elements = len(arr)  # Get the total number of elements in the array
    
    # Calculate the ratio of zeroes
    ratio = zeroes / total_elements
    return ratio

# Test case
assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.15
    assert zero_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.00
    assert zero_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.00
