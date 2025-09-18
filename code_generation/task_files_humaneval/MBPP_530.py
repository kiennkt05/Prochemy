# MBPP/530
### Completion
def negative_count(arr):
    """
    Calculate the ratio of negative numbers in the given array of integers.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    float: The ratio of negative numbers in the array.
    """
    if not arr:  # Check if the array is empty
        return 0.0  # Return 0.0 for an empty array

    total_count = len(arr)  # Total number of elements in the array
    negative_count = sum(1 for num in arr if num < 0)  # Count negative numbers

    # Calculate the ratio of negative numbers
    ratio = negative_count / total_count
    return round(ratio, 2)  # Round to 2 decimal places for clarity

# Test case
assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.31
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert negative_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.31
    assert negative_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.31
    assert negative_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.44
