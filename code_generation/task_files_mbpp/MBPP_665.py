# MBPP/665
### Completion
def move_last(lst):
    if lst:  # Check if the list is not empty
        return lst[1:] + [lst[0]]
    return lst  # Return the original list if it's empty

# Test the function with the provided assertion
assert move_last([1, 2, 3, 4]) == [2, 3, 4, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_last([1,2,3,4]) == [2,3,4,1]
    assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]
    assert move_last([5,4,3,2,1]) == [4,3,2,1,5]
