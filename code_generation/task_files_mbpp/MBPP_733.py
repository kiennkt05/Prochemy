# MBPP/733
### Completion
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # Initialize result to -1, indicating not found

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Update result to the current mid index
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return result

# Test the function with the provided assertion
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4
