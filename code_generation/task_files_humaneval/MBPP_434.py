# MBPP/434
### Completion
import re

def text_match_one(text):
    """
    Check if the input string matches the pattern of 'a' followed by one or more 'b's.
    
    Args:
    text (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether the string matched the pattern or not.
    """
    # Define the regex pattern for 'a' followed by one or more 'b's
    pattern = r'a+b+'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, text):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test case
assert text_match_one("ac") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_one("ac")==('Not matched!')
    assert text_match_one("dc")==('Not matched!')
    assert text_match_one("abba")==('Found a match!')
