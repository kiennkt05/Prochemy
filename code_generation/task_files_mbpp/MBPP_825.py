# MBPP/825
### Completion
def access_elements(lst, indices):
    return [lst[i] for i in indices]

# Test the function with the provided assertion
assert access_elements([2, 3, 8, 4, 7, 9], [0, 3, 5]) == [2, 4, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert access_elements([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]
    assert access_elements([1, 2, 3, 4, 5],[1,2]) == [2,3]
    assert access_elements([1,0,2,3],[0,1]) == [1,0]
