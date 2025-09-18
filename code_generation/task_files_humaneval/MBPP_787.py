# MBPP/787
### Completion
import re

def text_match_three(text):
    """
    Check if the input string contains an 'a' followed by exactly three 'b's.
    
    Args:
    text (str): The input string to be checked.
    
    Returns:
    str: 'Matched!' if the pattern is found, 'Not matched!' otherwise.
    """
    # Define the regex pattern for 'a' followed by exactly three 'b's
    pattern = r'a b{3}'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, text):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test case
assert text_match_three("ac") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_three("ac")==('Not matched!')
    assert text_match_three("dc")==('Not matched!')
    assert text_match_three("abbbba")==('Found a match!')
