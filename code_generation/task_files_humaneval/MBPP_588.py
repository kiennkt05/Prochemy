# MBPP/588
### Completion
def big_diff(arr):
    """
    Calculate the difference between the largest and smallest values in the array.

    Parameters:
    arr (list): A list of numbers.

    Returns:
    int: The difference between the largest and smallest values.
    """
    # Check if the array is empty
    if not arr:
        raise ValueError("The array should not be empty.")
    
    # Find the maximum and minimum values in the array
    largest = max(arr)
    smallest = min(arr)
    
    # Calculate the difference
    difference = largest - smallest
    
    return difference

# Test case
assert big_diff([1, 2, 3, 4]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert big_diff([1,2,3,4]) == 3
    assert big_diff([4,5,12]) == 8
    assert big_diff([9,2,3]) == 7
