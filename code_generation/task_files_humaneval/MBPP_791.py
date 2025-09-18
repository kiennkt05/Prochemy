# MBPP/791
### Completion
def remove_nested(input_tuple):
    """
    Remove nested tuples from the given tuple.

    Parameters:
    input_tuple (tuple): The input tuple potentially containing nested tuples.

    Returns:
    tuple: A new tuple with all nested tuples removed.
    """
    # Use a generator expression to filter out nested tuples
    return tuple(item for item in input_tuple if not isinstance(item, tuple))

# Test case
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)

# Additional test cases
assert remove_nested((1, (2, 3), 4, (5,))) == (1, 4)
assert remove_nested(((1, 2), (3, 4), 5)) == (5,)
assert remove_nested((1, 2, 3)) == (1, 2, 3)
assert remove_nested(()) == ()

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
