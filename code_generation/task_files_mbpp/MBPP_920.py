# MBPP/920
### Completion
def remove_tuple(tuple_list):
    # Filter out tuples that are all None
    filtered_tuples = [t for t in tuple_list if any(value is not None for value in t)]
    return str(filtered_tuples)

# Test the function with the provided assertion
assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )]) == '[(None, 2), (3, 4), (12, 3)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'
    assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'
    assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'
