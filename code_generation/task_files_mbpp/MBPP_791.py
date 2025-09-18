# MBPP/791
### Completion
def remove_nested(tup):
    # Use a generator expression to filter out nested tuples
    return tuple(item for item in tup if not isinstance(item, tuple))

# Test the function with the provided assertion
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)

# You can also add more test cases to verify the function
assert remove_nested((1, (2, 3), 4, (5,))) == (1, 4)
assert remove_nested(((1, 2), (3, 4), 5)) == (5,)
assert remove_nested((1, 2, 3)) == (1, 2, 3)
assert remove_nested(()) == ()
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
