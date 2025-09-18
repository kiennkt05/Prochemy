# MBPP/802
### Completion
def count_Rotation(arr):
    """
    Function to count the number of rotations required to generate a sorted array.
    
    Parameters:
    arr (list): The input array which is a rotated version of a sorted array.
    
    Returns:
    int: The number of rotations.
    """
    n = len(arr)
    
    # Edge case: If the array is empty or has one element, no rotations are needed
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    left, right = 0, n - 1
    
    # If the array is already sorted (no rotations)
    if arr[left] < arr[right]:
        return 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the minimum element
        if (mid == 0 or arr[mid] < arr[mid - 1]) and (mid == n - 1 or arr[mid] < arr[mid + 1]):
            return mid
        
        # Decide which half to continue searching
        if arr[mid] >= arr[left]:
            # Left half is sorted, so the minimum must be in the right half
            left = mid + 1
        else:
            # Right half is sorted, so the minimum must be in the left half
            right = mid - 1
    
    return 0  # This line should not be reached if the input is valid

# Test case
assert count_Rotation([3, 2, 1]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Rotation([3,2,1],3) == 1
    assert count_Rotation([4,5,1,2,3],5) == 2
    assert count_Rotation([7,8,9,1,2,3],6) == 3
