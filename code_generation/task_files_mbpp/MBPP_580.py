# MBPP/580
### Completion
def extract_even(nested_tuple):
    if isinstance(nested_tuple, tuple):
        return tuple(extract_even(item) for item in nested_tuple if isinstance(item, int) and item % 2 == 0 or isinstance(item, tuple) and extract_even(item))
    return ()

# Test the function with the provided assertion
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)
