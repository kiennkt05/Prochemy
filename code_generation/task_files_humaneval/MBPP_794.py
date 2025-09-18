# MBPP/794
### Completion
import re

def text_starta_endb(input_string):
    """
    Check if the input string starts with 'a' and ends with 'b'.
    
    Args:
    input_string (str): The string to be checked.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Regular expression pattern to match 'a' followed by anything and ending with 'b'
    pattern = r'^a.*b$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
assert text_starta_endb("aabbbb") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_starta_endb("aabbbb")==('Found a match!')
    assert text_starta_endb("aabAbbbc")==('Not matched!')
    assert text_starta_endb("accddbbjjj")==('Not matched!')
