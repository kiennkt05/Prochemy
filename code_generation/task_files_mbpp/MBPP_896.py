# MBPP/896
### Completion
def sort_list_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

# Test the function with the provided assertion
assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]) == [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])==[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
    assert sort_list_last([(9,8), (4, 7), (3,5), (7,9), (1,2)])==[(1,2), (3,5), (4,7), (9,8), (7,9)] 
    assert sort_list_last([(20,50), (10,20), (40,40)])==[(10,20),(40,40),(20,50)] 
