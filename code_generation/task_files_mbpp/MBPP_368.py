# MBPP/368
### Completion
def repeat_tuples(tup, n):
    return (tup,) * n

# Test the function with the provided assertion
assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
    assert repeat_tuples((1, 2), 3) == ((1, 2), (1, 2), (1, 2))
    assert repeat_tuples((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))
