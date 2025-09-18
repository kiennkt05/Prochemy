# MBPP/442
### Completion
def positive_count(arr):
    """
    Calculate the ratio of positive numbers in an array of integers.

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    float: The ratio of positive numbers in the array. Returns 0.0 if the array is empty.
    """
    if not arr:  # Check if the array is empty
        return 0.0

    total_count = len(arr)  # Total number of elements in the array
    positive_count = sum(1 for x in arr if x > 0)  # Count positive numbers

    # Calculate the ratio of positive numbers
    ratio = positive_count / total_count
    return ratio

# Test case
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56
