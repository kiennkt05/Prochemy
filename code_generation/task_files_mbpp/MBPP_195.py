# MBPP/195
### Completion
def first(arr, target, n):
    left, right = 0, n - 1
    result = -1  # Initialize result to -1, which indicates not found

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Update result to the current mid
            right = mid - 1  # Move left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Test the function with the provided assertion
assert first([1, 2, 3, 4, 5, 6, 6], 6, 6) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first([1,2,3,4,5,6,6],6,6) == 5
    assert first([1,2,2,2,3,2,2,4,2],2,9) == 1
    assert first([1,2,3],1,3) == 0
