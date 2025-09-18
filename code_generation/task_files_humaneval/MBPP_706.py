# MBPP/706
### Completion
def is_subset(arr1, size1, arr2, size2):
    """
    Check if arr2 is a subset of arr1.

    Parameters:
    arr1 (list): The first array.
    size1 (int): The size of the first array.
    arr2 (list): The second array.
    size2 (int): The size of the second array.

    Returns:
    bool: True if arr2 is a subset of arr1, False otherwise.
    """
    # Create a set from the first array for O(1) average time complexity lookups
    set_arr1 = set(arr1)
    
    # Check each element in arr2 to see if it exists in set_arr1
    for element in arr2:
        if element not in set_arr1:
            return False  # If any element is not found, return False
    
    return True  # All elements were found, so arr2 is a subset of arr1

# Test case
assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_subset([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4) == True
    assert is_subset([1, 2, 3, 4, 5, 6], 6, [1, 2, 4], 3) == True
    assert is_subset([10, 5, 2, 23, 19], 5, [19, 5, 3], 3) == False
