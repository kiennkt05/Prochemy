# MBPP/703
### Completion
def is_key_present(dictionary, key):
    """
    Check if the given key is present in the dictionary.

    Parameters:
    dictionary (dict): The dictionary to check.
    key: The key to look for in the dictionary.

    Returns:
    bool: True if the key is present, False otherwise.
    """
    return key in dictionary

# Test case
assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 5) == True

# Additional test cases for verification
assert is_key_present({1: 10, 2: 20, 3: 30}, 4) == False  # Key 4 is not present
assert is_key_present({}, 1) == False  # Empty dictionary, key 1 is not present
assert is_key_present({1: 10}, 1) == True  # Key 1 is present
assert is_key_present({1: 10, 2: 20}, 2) == True  # Key 2 is present

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)==True
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},6)==True
    assert is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},10)==False
