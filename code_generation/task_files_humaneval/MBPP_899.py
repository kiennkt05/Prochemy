# MBPP/899
### Completion
def check(arr, n):
    # Check if the array is empty or has only one element
    if n <= 1:
        return True
    
    # Get the corner elements
    left = arr[0]
    right = arr[-1]
    
    # Create a new list to store the sorted version of the array
    sorted_arr = sorted(arr)
    
    # Check if we can form the sorted array using only corner elements
    # We can only take elements from the start or the end of the original array
    can_sort = True
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            # If the current element is not in the sorted array, check if it can be from corners
            if arr[i] != left and arr[i] != right:
                can_sort = False
                break
    
    return can_sort

# Test case
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
