# MBPP/793
### Completion
def last(arr, target, n):
    """
    Find the last position of an element in a sorted array.

    Parameters:
    arr (list): A sorted list of integers.
    target (int): The element to find the last position of.
    n (int): The length of the array.

    Returns:
    int: The last index of the target in the array, or -1 if not found.
    """
    left, right = 0, n - 1
    last_index = -1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            last_index = mid  # Update last_index when target is found
            left = mid + 1    # Continue searching to the right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_index

# Test case
assert last([1, 2, 3], 1, 3) == 0  # The last position of 1 is at index 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last([1,2,3],1,3) == 0
    assert last([1,1,1,2,3,4],1,6) == 2
    assert last([2,3,2,3,6,8,9],3,8) == 3
