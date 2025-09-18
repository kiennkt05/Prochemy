# MBPP/43
### Completion
import re

def text_match(text):
    """
    Check if the input text consists of sequences of lowercase letters joined by underscores.
    
    Args:
    text (str): The input string to check.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Define the regex pattern for matching sequences of lowercase letters joined by underscores
    pattern = r'^[a-z]+(_[a-z]+)*$'
    
    # Use re.match to check if the entire string matches the pattern
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided test case
assert text_match("aab_cbbbc") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match("aab_cbbbc") == 'Found a match!'
    assert text_match("aab_Abbbc") == 'Not matched!'
    assert text_match("Aaab_abbbc") == 'Not matched!'
