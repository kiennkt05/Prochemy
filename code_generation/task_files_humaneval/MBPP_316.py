# MBPP/316
### Completion
def find_last_occurrence(arr, target):
    """
    Find the index of the last occurrence of a given number in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The number to find the last occurrence of.

    Returns:
    int: The index of the last occurrence of target in arr, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    last_index = -1  # Initialize last_index to -1 (not found)

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            last_index = mid  # Update last_index if target is found
            left = mid + 1    # Continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1    # Move to the right half
        else:
            right = mid - 1   # Move to the left half

    return last_index

# Test case
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
