# MBPP/280
### Completion
def sequential_search(arr, target):
    """
    Perform a sequential search for the target in the given array.

    Parameters:
    arr (list): The list of elements to search through.
    target: The element to search for in the list.

    Returns:
    tuple: A tuple containing a boolean indicating if the target was found,
           and the index of the target if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return (True, index)  # Target found, return True and the index
    return (False, -1)  # Target not found, return False and -1

# Test case
assert sequential_search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31) == (True, 3)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)
