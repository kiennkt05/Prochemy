# MBPP/382
### Completion
def find_rotation_count(arr):
    left, right = 0, len(arr) - 1
    
    # Handle cases where the array is not rotated at all
    if arr[left] < arr[right]:
        return 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the minimum element
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        if arr[mid] < arr[mid - 1]:
            return mid
        
        # Decide which half to continue searching
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1
            
    return 0  # This line should never be reached if the input is valid

# Test the function with the provided assertion
assert find_rotation_count([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_rotation_count([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]) == 3
    assert find_rotation_count([8, 9, 10,2, 5, 6]) == 3
    assert find_rotation_count([2, 5, 6, 8, 9, 10]) == 0
