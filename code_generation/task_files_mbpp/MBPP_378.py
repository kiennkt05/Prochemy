# MBPP/378
### Completion
def move_first(lst):
    if lst:  # Check if the list is not empty
        return [lst[-1]] + lst[:-1]  # Move last element to the front
    return lst  # Return the original list if it's empty

# Test the function with the provided assertion
assert move_first([1, 2, 3, 4]) == [4, 1, 2, 3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_first([1,2,3,4]) == [4,1,2,3]
    assert move_first([0,1,2,3]) == [3,0,1,2]
    assert move_first([9,8,7,1]) == [1,9,8,7]
