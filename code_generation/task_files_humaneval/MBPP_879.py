# MBPP/879
### Completion
import re

def text_match(s):
    """
    Check if the string starts with 'a' and ends with 'b'.
    
    Args:
    s (str): The input string to check.
    
    Returns:
    str: 'Matched!' if the pattern is found, otherwise 'Not matched!'.
    """
    # Regular expression pattern to match 'a' followed by anything and ending with 'b'
    pattern = r'^a.*b$'
    
    # Use re.match to check if the pattern matches the entire string
    if re.match(pattern, s):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test case
assert text_match("aabbbbd") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match("aabbbbd") == 'Not matched!'
    assert text_match("aabAbbbc") == 'Not matched!'
    assert text_match("accddbbjjjb") == 'Found a match!'
