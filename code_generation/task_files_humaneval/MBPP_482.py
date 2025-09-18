# MBPP/482
### Completion
import re

def match(s):
    """
    Check if the input string matches the pattern of one uppercase letter followed by lowercase letters.
    
    Args:
    s (str): The input string to check.
    
    Returns:
    str: 'Yes' if the string matches the pattern, 'No' otherwise.
    """
    # Define the regex pattern
    pattern = r'^[A-Z][a-z]*$'
    
    # Use re.match to check if the entire string matches the pattern
    if re.match(pattern, s):
        return 'Yes'
    else:
        return 'No'

# Test case
assert match("Geeks") == 'Yes'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert match("Geeks") == 'Yes'
    assert match("geeksforGeeks") == 'Yes'
    assert match("geeks") == 'No'
