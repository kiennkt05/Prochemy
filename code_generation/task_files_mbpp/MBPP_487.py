# MBPP/487
### Completion
def sort_tuple(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

# Test the function with the provided assertion
assert sort_tuple([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_tuple([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]
    assert sort_tuple([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]
    assert sort_tuple([(3, 9), (6, 7), (4, 3)] ) == [(4, 3), (6, 7), (3, 9)]
