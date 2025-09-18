# MBPP/421
### Completion
def concatenate_tuple(tup, delimiter='-'):
    # Convert all elements to string and join them with the delimiter
    return delimiter.join(map(str, tup))

# Test the function with the provided assertion
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'
