# MBPP/852
### Completion
def remove_negs(lst):
    """Remove negative numbers from a list."""
    return [num for num in lst if num >= 0]

# Test the function with the provided assertion
assert remove_negs([1, -2, 3, -4]) == [1, 3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_negs([1,-2,3,-4]) == [1,3]
    assert remove_negs([1,2,3,-4]) == [1,2,3]
    assert remove_negs([4,5,-6,7,-8]) == [4,5,7]
