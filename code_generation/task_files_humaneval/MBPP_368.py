# MBPP/368
### Completion
def repeat_tuples(input_tuple, n):
    """
    Repeat the given tuple n times.

    Parameters:
    input_tuple (tuple): The tuple to be repeated.
    n (int): The number of times to repeat the tuple.

    Returns:
    tuple: A new tuple containing the input tuple repeated n times.
    """
    return input_tuple * n

# Test case
assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))

# Additional test cases
assert repeat_tuples(('a', 'b'), 3) == (('a', 'b'), ('a', 'b'), ('a', 'b'))
assert repeat_tuples((), 5) == ((), (), (), (), ())
assert repeat_tuples((1,), 0) == ()
assert repeat_tuples((True, False), 2) == ((True, False), (True, False))

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
    assert repeat_tuples((1, 2), 3) == ((1, 2), (1, 2), (1, 2))
    assert repeat_tuples((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))
