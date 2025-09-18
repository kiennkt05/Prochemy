# MBPP/304
### Completion
def find_Element(arr, rotations, n, index):
    # Calculate the effective number of rotations
    effective_rotations = sum(rot[1] for rot in rotations) % n
    
    # Calculate the new index after rotations
    new_index = (index - effective_rotations + n) % n
    
    # Return the element at the new index
    return arr[new_index]

# Test the function with the provided assertion
assert find_Element([1, 2, 3, 4, 5], [[0, 2], [0, 3]], 5, 1) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
