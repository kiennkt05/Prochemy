# MBPP/341
### Completion
def set_to_tuple(input_set):
    # Convert the set to a sorted list and then to a tuple
    return tuple(sorted(input_set))

# Test the function with the provided assertion
assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
    assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
    assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)
