# MBPP/744
### Completion
def check_none(tup):
    return any(item is None for item in tup)

# Test the function with the provided assertion
assert check_none((10, 4, 5, 6, None)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_none((10, 4, 5, 6, None)) == True
    assert check_none((7, 8, 9, 11, 14)) == False
    assert check_none((1, 2, 3, 4, None)) == True
