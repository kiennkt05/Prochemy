# MBPP/942
### Completion
def check_element(tup, lst):
    """
    Check if any element from the given tuple is present in the provided list.

    Parameters:
    tup (tuple): A tuple containing elements to check.
    lst (list): A list in which to check for the presence of tuple elements.

    Returns:
    bool: True if any element from the tuple is found in the list, False otherwise.
    """
    # Check if any element in the tuple is in the list
    for element in tup:
        if element in lst:
            return True
    return False

# Test case
assert check_element((4, 5, 7, 9, 3), [6, 7, 10, 11]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_element((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True
    assert check_element((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True
    assert check_element((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False
