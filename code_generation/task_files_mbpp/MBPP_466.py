# MBPP/466
### Completion
def find_peak(arr, n):
    if n == 1:
        return 0  # The only element is the peak
    
    if arr[0] >= arr[1]:
        return 0  # The first element is a peak
    
    if arr[n - 1] >= arr[n - 2]:
        return n - 1  # The last element is a peak
    
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i  # Found a peak
    
    return -1  # This line should never be reached if the input is valid

# Test the function with the provided assertion
assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2
    assert find_peak([2, 3, 4, 5, 6], 5) == 4
    assert find_peak([8, 9, 11, 12, 14, 15], 6) == 5 
