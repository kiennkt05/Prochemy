# MBPP/733
### Completion
def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a given number in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The number to find in the array.

    Returns:
    int: The index of the first occurrence of target in arr, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    result = -1  # Initialize result to -1 (not found)

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid index

        if arr[mid] == target:
            result = mid  # Update result to current mid
            right = mid - 1  # Move left to find first occurrence
        elif arr[mid] < target:
            left = mid + 1  # Move right
        else:
            right = mid - 1  # Move left

    return result

# Test case
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
