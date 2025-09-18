# MBPP/396
### Completion
import re

def check_char(s):
    """
    Check if the given string starts and ends with the same character.
    
    Args:
    s (str): The input string to check.
    
    Returns:
    str: "Valid" if the first and last characters are the same, "Invalid" otherwise.
    """
    # Regex pattern to match if the first and last character are the same
    pattern = r'^(?P<first>.)(?P=first).*?(?P=first)$'
    
    # Use re.match to check the pattern against the string
    if re.match(pattern, s):
        return "Valid"
    else:
        return "Invalid"

# Test case
assert check_char("abba") == "Valid"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"
