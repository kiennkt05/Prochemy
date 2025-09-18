# MBPP/972
### Completion
def concatenate_nested(tuple1, tuple2):
    return tuple1 + tuple2

# Test the function with the provided assertion
assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_nested((3, 4), (5, 6)) == (3, 4, 5, 6)
    assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert concatenate_nested((4, 5), (6, 8)) == (4, 5, 6, 8)
