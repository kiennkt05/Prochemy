# MBPP/145
### Completion
def max_Abs_Diff(arr, n):
    # Check if the array is empty or has less than 2 elements
    if len(arr) < 2:
        return 0
    
    # Find the maximum and minimum elements in the array
    max_element = max(arr)
    min_element = min(arr)
    
    # Calculate the maximum absolute difference
    max_difference = max_element - min_element
    
    return max_difference

# Test the function with the provided assertion
assert max_Abs_Diff((2, 1, 5, 3), 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_Abs_Diff((2,1,5,3),4) == 4
    assert max_Abs_Diff((9,3,2,5,1),5) == 8
    assert max_Abs_Diff((3,2,1),3) == 2
