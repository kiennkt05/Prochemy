# MBPP/792
### Completion
def count_list(lists):
    return len(lists)

# Test the function with the provided assertion
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert count_list([[1,2],[2,3],[4,5]]) == 3
    assert count_list([[1,0],[2,0]]) == 2
