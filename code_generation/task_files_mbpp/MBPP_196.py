# MBPP/196
### Completion
def remove_tuples(tuples_list, k):
    return [t for t in tuples_list if len(t) != k]

# Test the function with the provided assertion
assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] , 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]
    assert remove_tuples([(4, 5), (4,5), (6, 7), (1, 2, 3), (3, 4, 6, 7)] ,2) == [(1, 2, 3), (3, 4, 6, 7)]
    assert remove_tuples([(1, 4, 4), (4, 3), (8, 6, 7), (1, ), (3, 6, 7)] , 3) == [(4, 3), (1,)]
