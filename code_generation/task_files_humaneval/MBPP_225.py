# MBPP/225
### Completion
def find_Min(arr, low, high):
    """
    Function to find the minimum element in a sorted and rotated array.
    
    Parameters:
    arr (list): The sorted and rotated array.
    low (int): The starting index of the array.
    high (int): The ending index of the array.
    
    Returns:
    int: The minimum element in the array.
    """
    # If the array is not rotated
    if high < low:
        return arr[0]
    
    if high == low:
        return arr[low]
    
    mid = (low + high) // 2
    
    # Check if mid is the minimum element
    if mid < high and arr[mid + 1] < arr[mid]:
        return arr[mid + 1]
    
    # Check if mid-1 is the minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]
    
    # Decide whether to go to the left half or the right half
    if arr[high] > arr[mid]:
        return find_Min(arr, low, mid - 1)
    else:
        return find_Min(arr, mid + 1, high)

# Test case
assert find_Min([1, 2, 3, 4, 5], 0, 4) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min([1,2,3,4,5],0,4) == 1
    assert find_Min([4,6,8],0,2) == 4
    assert find_Min([2,3,5,7,9],0,4) == 2
