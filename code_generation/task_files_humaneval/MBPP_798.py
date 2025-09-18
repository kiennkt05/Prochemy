# MBPP/798
### Completion
def _sum(array):
    """
    Calculate the sum of elements in the given array.

    Parameters:
    array (list): A list of numbers to sum up.

    Returns:
    int or float: The sum of the elements in the array.
    """
    return sum(array)

# Test case
assert _sum([1, 2, 3]) == 6  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert _sum([1, 2, 3]) == 6
    assert _sum([15, 12, 13, 10]) == 50
    assert _sum([0, 1, 2]) == 3
