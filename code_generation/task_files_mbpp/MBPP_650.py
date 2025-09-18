# MBPP/650
### Completion
def are_Equal(arr1, arr2, n, m):
    # Check if the lengths of the arrays are different
    if n != m:
        return False
    
    # Sort both arrays and compare them
    return sorted(arr1) == sorted(arr2)

# Test the function with the provided assertion
assert are_Equal([1, 2, 3], [3, 2, 1], 3, 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert are_Equal([1,2,3],[3,2,1],3,3) == True
    assert are_Equal([1,1,1],[2,2,2],3,3) == False
    assert are_Equal([8,9],[4,5,6],2,3) == False
