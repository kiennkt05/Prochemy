# MBPP/899
### Completion
def check(arr, n):
    # If the array has less than 2 elements, it is trivially sortable
    if n < 2:
        return True
    
    # Create a new array using only the corner elements
    corner_elements = [arr[0], arr[-1]]
    
    # Sort the corner elements
    sorted_corners = sorted(corner_elements)
    
    # Check if the original array can be sorted using the corner elements
    # We can only replace the first and last elements with the sorted corners
    new_array = [sorted_corners[0]] + arr[1:-1] + [sorted_corners[1]]
    
    # Check if the new array is sorted
    return new_array == sorted(new_array)

# Test the function with the provided assertion
assert check([3, 2, 1, 2, 3, 4], 6) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check([3,2,1,2,3,4],6) == True
    assert check([2,1,4,5,1],5) == True
    assert check([1,2,2,1,2,3],6) == True
