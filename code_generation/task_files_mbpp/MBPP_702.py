# MBPP/702
### Completion
def removals(arr, n, k):
    # Sort the array
    arr.sort()
    
    left = 0
    max_length = 0
    
    # Use two pointers to find the longest valid subarray
    for right in range(len(arr)):
        # While the condition is not met, move the left pointer
        while arr[right] - arr[left] > k:
            left += 1
        # Calculate the length of the current valid subarray
        max_length = max(max_length, right - left + 1)
    
    # The number of elements to remove is the total elements minus the length of the longest valid subarray
    return len(arr) - max_length

# Test the function with the provided assertion
assert removals([1, 3, 4, 9, 10, 11, 12, 17, 20], 9, 4) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert removals([1, 3, 4, 9, 10,11, 12, 17, 20], 9, 4) == 5
    assert removals([1, 5, 6, 2, 8], 5, 2) == 3
    assert removals([1, 2, 3 ,4, 5, 6], 6, 3) == 2
