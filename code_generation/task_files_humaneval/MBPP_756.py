# MBPP/756
### Completion
import re

def text_match_zero_one(text):
    """
    This function checks if the input string contains 'a' followed by zero or one 'b'.
    
    Parameters:
    text (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Define the regex pattern for 'a' followed by zero or one 'b'
    pattern = r'a(b)?'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
assert text_match_zero_one("ac") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_zero_one("ac")==('Found a match!')
    assert text_match_zero_one("dc")==('Not matched!')
    assert text_match_zero_one("abbbba")==('Found a match!')
