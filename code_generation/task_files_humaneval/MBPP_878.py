# MBPP/878
### Completion
def check_tuples(tup, allowed_elements):
    """
    Check if the given tuple contains only elements from the allowed_elements list.

    Parameters:
    tup (tuple): The tuple to check.
    allowed_elements (list): The list of allowed elements.

    Returns:
    bool: True if the tuple contains only allowed elements, False otherwise.
    """
    # Convert the list of allowed elements to a set for faster lookup
    allowed_set = set(allowed_elements)
    
    # Check if all elements in the tuple are in the allowed set
    for element in tup:
        if element not in allowed_set:
            return False
    return True

# Test case
assert check_tuples((3, 5, 6, 5, 3, 6), [3, 6, 5]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_tuples((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True
    assert check_tuples((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True
    assert check_tuples((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False
