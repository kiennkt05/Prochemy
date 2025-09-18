# MBPP/793
### Completion
def last(arr, target, n):
    left, right = 0, n - 1
    last_position = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            last_position = mid  # Update last_position
            left = mid + 1  # Move to the right half to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last_position

# Test the function with the provided assertion
assert last([1, 2, 3], 1, 3) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last([1,2,3],1,3) == 0
    assert last([1,1,1,2,3,4],1,6) == 2
    assert last([2,3,2,3,6,8,9],3,8) == 3
