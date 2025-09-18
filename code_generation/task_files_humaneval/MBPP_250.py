# MBPP/250
### Completion
def count_X(tup, element):
    """
    Count the occurrences of an element in a tuple.

    Parameters:
    tup (tuple): The tuple in which to count occurrences.
    element: The element to count in the tuple.

    Returns:
    int: The number of occurrences of the element in the tuple.
    """
    return tup.count(element)

# Test case
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4) == 0

# Additional test cases for verification
assert count_X((1, 2, 3, 4, 5, 1, 1), 1) == 3  # 1 occurs 3 times
assert count_X((1, 2, 3, 4, 5), 6) == 0          # 6 does not occur
assert count_X((), 1) == 0                       # Empty tuple
assert count_X((1, 1, 1, 1), 1) == 4             # 1 occurs 4 times

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4
