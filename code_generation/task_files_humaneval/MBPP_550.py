# MBPP/550
### Completion
def find_Max(arr, low, high):
    """
    Function to find the maximum element in a sorted and rotated array.
    
    Parameters:
    arr (list): The input array which is sorted and rotated.
    low (int): The starting index of the array segment to search.
    high (int): The ending index of the array segment to search.
    
    Returns:
    int: The maximum element in the array.
    """
    # If the array is not rotated (the first element is less than the last)
    if low > high:
        return None  # Invalid case

    if low == high:
        return arr[low]  # Only one element

    mid = (low + high) // 2

    # Check if mid is the maximum
    if mid < high and arr[mid] > arr[mid + 1]:
        return arr[mid]
    
    # Check if mid-1 is the maximum
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid - 1]

    # Decide which half to continue searching
    if arr[low] >= arr[mid]:
        return find_Max(arr, low, mid - 1)  # Search in the left half
    else:
        return find_Max(arr, mid + 1, high)  # Search in the right half

# Test case
assert find_Max([2, 3, 5, 6, 9], 0, 4) == 9
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Max([2,3,5,6,9],0,4) == 9
    assert find_Max([3,4,5,2,1],0,4) == 5
    assert find_Max([1,2,3],0,2) == 3
