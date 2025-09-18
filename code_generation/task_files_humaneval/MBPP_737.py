# MBPP/737
### Completion
import re

def check_str(s):
    """
    Check if the given string starts with a vowel.

    Parameters:
    s (str): The input string to check.

    Returns:
    str: 'Valid' if the string starts with a vowel, 'Invalid' otherwise.
    """
    # Define the regex pattern to match a string starting with a vowel
    pattern = r'^[aeiouAEIOU]'
    
    # Use re.match to check if the string starts with a vowel
    if re.match(pattern, s):
        return 'Valid'
    else:
        return 'Invalid'

# Test case
assert check_str("annie") == 'Valid'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_str("annie") == 'Valid'
    assert check_str("dawood") == 'Invalid'
    assert check_str("Else") == 'Valid'
