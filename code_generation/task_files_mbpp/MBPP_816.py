# MBPP/816
### Completion
def clear_tuple(t):
    return ()

# Test the function
assert clear_tuple((1, 5, 3, 6, 8)) == ()
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert clear_tuple((1, 5, 3, 6, 8)) == ()
    assert clear_tuple((2, 1, 4 ,5 ,6)) == ()
    assert clear_tuple((3, 2, 5, 6, 8)) == ()
