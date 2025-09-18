# MBPP/316
### Completion
def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    last_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            last_index = mid  # Update last_index when target is found
            left = mid + 1    # Move to the right side to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last_index

# Test the function with the provided assertion
assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_last_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 3
    assert find_last_occurrence([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9) == 9
    assert find_last_occurrence([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6) == 6
