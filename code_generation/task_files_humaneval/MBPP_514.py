# MBPP/514
### Completion
def sum_elements(tup):
    """
    Calculate the summation of elements in a given tuple.

    Parameters:
    tup (tuple): A tuple containing numeric elements.

    Returns:
    int or float: The sum of the elements in the tuple.
    """
    return sum(tup)

# Test case
assert sum_elements((7, 8, 9, 1, 10, 7)) == 42

# Additional test cases for verification
assert sum_elements((1, 2, 3)) == 6
assert sum_elements((0, 0, 0)) == 0
assert sum_elements((-1, -2, -3)) == -6
assert sum_elements((10.5, 2.5)) == 13.0

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_elements((7, 8, 9, 1, 10, 7)) == 42
    assert sum_elements((1, 2, 3, 4, 5, 6)) == 21
    assert sum_elements((11, 12 ,13 ,45, 14)) == 95
