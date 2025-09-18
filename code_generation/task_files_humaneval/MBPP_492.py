# MBPP/492
### Completion
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Parameters:
    arr (list): A list of sorted elements.
    target (int): The element to search for.

    Returns:
    bool: True if the target is found, False otherwise.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        mid_value = arr[mid]  # Get the middle value
        
        if mid_value == target:
            return True  # Target found
        elif mid_value < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return False  # Target not found

# Test case
assert binary_search([1, 2, 3, 5, 8], 6) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_search([1,2,3,5,8], 6) == False
    assert binary_search([7, 8, 9, 10, 13], 10) == True
    assert binary_search([11, 13, 14, 19, 22, 36], 23) == False
