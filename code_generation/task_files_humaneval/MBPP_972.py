# MBPP/972
### Completion
def concatenate_nested(tuple1, tuple2):
    """
    Concatenates two tuples into a single nested tuple.

    Parameters:
    tuple1 (tuple): The first tuple to concatenate.
    tuple2 (tuple): The second tuple to concatenate.

    Returns:
    tuple: A new tuple that is the concatenation of tuple1 and tuple2.
    """
    # Concatenate the two tuples
    result = tuple1 + tuple2
    return result

# Test case
assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)

# Additional test cases for verification
assert concatenate_nested((), ()) == ()  # Concatenating two empty tuples
assert concatenate_nested((1,), (2,)) == (1, 2)  # Concatenating single-element tuples
assert concatenate_nested((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)  # Concatenating tuples of different lengths

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)
    assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert concatenate_nested((4, 5), (6, 8)) == (4, 5, 6, 8)
