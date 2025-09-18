# MBPP/304
### Completion
def find_Element(arr, queries, n, m):
    results = []
    length = len(arr)
    
    for rotations, index in queries:
        # Calculate the effective number of rotations
        effective_rotations = rotations % length
        
        # Calculate the new index after rotations
        new_index = (index - effective_rotations + length) % length
        
        # Append the result for the current query
        results.append(arr[new_index])
    
    return results[m]

# Test case
assert find_Element([1, 2, 3, 4, 5], [[0, 2], [0, 3]], 2, 1) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
