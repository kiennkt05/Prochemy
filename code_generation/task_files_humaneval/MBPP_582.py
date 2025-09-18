# MBPP/582
### Completion
def is_empty_dict(d):
    """
    Check if the provided dictionary is empty.

    Parameters:
    d (dict): The dictionary to check.

    Returns:
    bool: True if the dictionary is empty, False otherwise.
    """
    return len(d) == 0

# Test cases
assert is_empty_dict({}) == True  # An empty dictionary should return True
assert is_empty_dict({10: 'value'}) == False  # A non-empty dictionary should return False
assert is_empty_dict({'key': 10}) == False  # Another non-empty dictionary
assert is_empty_dict({'a': 1, 'b': 2}) == False  # Yet another non-empty dictionary

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True
