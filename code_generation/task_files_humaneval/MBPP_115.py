# MBPP/115
### Completion
def empty_dit(dict_list):
    """
    Check if all dictionaries in the provided list are empty.

    Parameters:
    dict_list (list): A list of dictionaries to check.

    Returns:
    bool: True if all dictionaries are empty, False otherwise.
    """
    for d in dict_list:
        if d:  # If the dictionary is not empty
            return False
    return True  # All dictionaries are empty

# Test case
assert empty_dit([{}, {}, {}]) == True  # All dictionaries are empty
assert empty_dit([{}, {'key': 'value'}, {}]) == False  # One dictionary is not empty
assert empty_dit([{'key': 'value'}, {}, {}]) == False  # One dictionary is not empty
assert empty_dit([]) == True  # An empty list should return True

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True
