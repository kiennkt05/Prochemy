# MBPP/371
### Completion
def smallest_missing(arr, left, right):
    # If the array is empty, the smallest missing element is 0
    if not arr:
        return 0
    
    # If the last element is equal to its index, the smallest missing element is after the last index
    if arr[right] == right:
        return right + 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the mid index matches the value at mid
        if arr[mid] == mid:
            # If it matches, search in the right half
            left = mid + 1
        else:
            # If it doesn't match, search in the left half
            right = mid - 1
            
    # The smallest missing element is the left index
    return left

# Test the function with the provided assertion
assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_missing([0, 1, 2, 3, 4, 5, 6], 0, 6) == 7
    assert smallest_missing([0, 1, 2, 6, 9, 11, 15], 0, 6) == 3
    assert smallest_missing([1, 2, 3, 4, 6, 9, 11, 15], 0, 7) == 0
