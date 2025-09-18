# MBPP/223
### Completion
def is_majority(arr, n, target):
    """
    Check if the target element is a majority element in the sorted array.

    Parameters:
    arr (list): The sorted array of integers.
    n (int): The size of the array.
    target (int): The element to check for majority.

    Returns:
    bool: True if target is a majority element, False otherwise.
    """
    
    def find_first_occurrence(arr, target):
        """Find the first occurrence of target in arr using binary search."""
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                if mid == 0 or arr[mid - 1] < target:
                    return mid
                high = mid - 1
        return -1

    def find_last_occurrence(arr, target):
        """Find the last occurrence of target in arr using binary search."""
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                if mid == n - 1 or arr[mid + 1] > target:
                    return mid
                low = mid + 1
        return -1

    first_index = find_first_occurrence(arr, target)
    if first_index == -1:
        return False  # target not found in the array

    last_index = find_last_occurrence(arr, target)
    count = last_index - first_index + 1

    return count > n // 2

# Test case
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
