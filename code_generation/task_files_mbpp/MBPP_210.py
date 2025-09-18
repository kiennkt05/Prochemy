# MBPP/210
### Completion
import re

def is_allowed_specific_char(s):
    # Define the regex pattern for allowed characters
    pattern = r'^[A-Za-z0-9]+$'
    # Use re.match to check if the entire string matches the pattern
    return bool(re.match(pattern, s))

# Test the function with the provided assertion
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
