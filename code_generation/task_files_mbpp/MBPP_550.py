# MBPP/550
### Completion
def find_Max(arr, low, high):
    # If the array is not rotated at all
    if high < low:
        return arr[0]
    
    # If there is only one element
    if high == low:
        return arr[low]
    
    mid = (low + high) // 2
    
    # Check if mid is the maximum element
    if mid < high and arr[mid] > arr[mid + 1]:
        return arr[mid]
    
    # Check if mid-1 is the maximum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid - 1]
    
    # Decide whether to go to the left half or the right half
    if arr[low] >= arr[mid]:
        return find_Max(arr, low, mid - 1)
    else:
        return find_Max(arr, mid + 1, high)

# Example usage
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
