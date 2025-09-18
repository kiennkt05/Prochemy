# MBPP/477
### Completion
def is_lower(input_string):
    """
    Convert the given string to lower case.

    Parameters:
    input_string (str): The string to be converted to lower case.

    Returns:
    str: The lower case version of the input string.
    """
    return input_string.lower()

# Test case
assert is_lower("InValid") == "invalid", "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"
