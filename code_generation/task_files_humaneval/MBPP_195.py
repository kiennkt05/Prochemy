# MBPP/195
### Completion
def first(arr, target, n):
    """
    Find the first position of an element in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The element to find.
    n (int): The length of the array.

    Returns:
    int: The index of the first occurrence of the target in the array, or -1 if not found.
    """
    left, right = 0, n - 1
    result = -1  # Initialize result to -1 (not found)

    while left <= right:
        mid = left + (right - left) // 2  # Calculate mid index

        if arr[mid] == target:
            result = mid  # Update result to current mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return result

# Test case
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
