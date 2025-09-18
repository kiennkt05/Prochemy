# MBPP/50
### Completion
def min_length_list(lists):
    return min((len(lst), lst) for lst in lists)

# Test the function with the provided assertion
assert min_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (1, [0])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
    assert min_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(1,[1])
    assert min_length_list([[3,4,5],[6,7,8,9],[10,11,12],[1,2]])==(2,[1,2])
