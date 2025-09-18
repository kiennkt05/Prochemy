# MBPP/744
### Completion
def check_none(input_tuple):
    """
    Check if the given tuple contains any None values.

    Parameters:
    input_tuple (tuple): The tuple to check for None values.

    Returns:
    bool: True if there is at least one None value, False otherwise.
    """
    # Iterate through each element in the tuple
    for item in input_tuple:
        # Check if the current item is None
        if item is None:
            return True  # Return True if None is found
    return False  # Return False if no None is found

# Test case
assert check_none((10, 4, 5, 6, None)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_none((10, 4, 5, 6, None)) == True
    assert check_none((7, 8, 9, 11, 14)) == False
    assert check_none((1, 2, 3, 4, None)) == True
