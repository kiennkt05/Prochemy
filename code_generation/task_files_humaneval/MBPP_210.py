# MBPP/210
### Completion
import re

def is_allowed_specific_char(s):
    """
    Check if the given string contains only characters a-z, A-Z, and 0-9.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string contains only allowed characters, False otherwise.
    """
    # Define the regex pattern for allowed characters
    pattern = r'^[a-zA-Z0-9]+$'
    
    # Use re.match to check if the entire string matches the pattern
    return bool(re.match(pattern, s))

# Test case
assert is_allowed_specific_char("ABCDEFabcdef123450") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_allowed_specific_char("ABCDEFabcdef123450") == True
    assert is_allowed_specific_char("*&%@#!}{") == False
    assert is_allowed_specific_char("HELLOhowareyou98765") == True
