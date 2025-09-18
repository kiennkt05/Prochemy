# MBPP/222
### Completion
def check_type(input_tuple):
    """
    Check if all elements in the tuple have the same data type.

    Parameters:
    input_tuple (tuple): The tuple to check.

    Returns:
    bool: True if all elements have the same type, False otherwise.
    """
    if not input_tuple:  # Check if the tuple is empty
        return True  # An empty tuple can be considered as having the same type

    first_type = type(input_tuple[0])  # Get the type of the first element

    # Check if all elements have the same type
    for element in input_tuple:
        if type(element) != first_type:
            return False  # Found an element with a different type

    return True  # All elements have the same type

# Test case
assert check_type((5, 6, 7, 3, 5, 6)) == True  # All elements are integers
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True
