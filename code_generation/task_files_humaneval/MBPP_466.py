# MBPP/466
### Completion
def find_peak(arr, n):
    """
    Function to find the index of a peak element in the given array.
    
    A peak element is defined as an element that is not smaller than its neighbors.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the array.
    
    Returns:
    int: The index of a peak element, or -1 if no peak exists.
    """
    if n == 0:
        return -1  # No elements in the array
    if n == 1:
        return 0  # Only one element, which is a peak by default

    # Check if the first element is a peak
    if arr[0] >= arr[1]:
        return 0

    # Check if the last element is a peak
    if arr[n - 1] >= arr[n - 2]:
        return n - 1

    # Check for peak elements in the middle of the array
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i

    return -1  # No peak found

# Test case
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
