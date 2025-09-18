# MBPP/802
### Completion
def count_Rotation(arr, n):
    # Function to find the index of the minimum element in the rotated sorted array
    def find_min_index(arr, low, high):
        if high < low:
            return 0
        if high == low:
            return low
        
        mid = (low + high) // 2
        
        # Check if mid is the minimum element
        if mid < high and arr[mid + 1] < arr[mid]:
            return mid + 1
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid
        
        # Decide whether to go to the left half or the right half
        if arr[high] > arr[mid]:
            return find_min_index(arr, low, mid - 1)
        return find_min_index(arr, mid + 1, high)

    return find_min_index(arr, 0, n - 1)

# Test the function with the provided assertion
assert count_Rotation([3, 2, 1], 3) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Rotation([3,2,1],3) == 1
    assert count_Rotation([4,5,1,2,3],5) == 2
    assert count_Rotation([7,8,9,1,2,3],6) == 3
