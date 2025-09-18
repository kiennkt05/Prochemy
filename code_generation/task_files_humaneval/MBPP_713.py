# MBPP/713
### Completion
def check_valid(values):
    """
    Check if all elements in the given tuple are boolean values.

    Args:
    values (tuple): A tuple containing elements to check.

    Returns:
    bool: True if all elements are boolean, False otherwise.
    """
    # Check if all elements in the tuple are instances of bool
    return all(isinstance(value, bool) for value in values)

# Test cases
assert check_valid((True, True, True, True)) == True
assert check_valid((True, False, True)) == True
assert check_valid((True, 1, False)) == False
assert check_valid((False, None, True)) == False
assert check_valid(()) == True  # An empty tuple should return True

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_valid((True, True, True, True) ) == True
    assert check_valid((True, False, True, True) ) == False
    assert check_valid((True, True, True, True) ) == True
