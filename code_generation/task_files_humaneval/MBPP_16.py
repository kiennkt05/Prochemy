# MBPP/16
### Completion
import re

def text_lowercase_underscore(text):
    """
    This function checks if the input string contains sequences of lowercase letters
    joined with an underscore. If such a sequence is found, it returns 'Found a match!'.
    
    Parameters:
    text (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Regular expression pattern to match sequences of lowercase letters joined by underscores
    pattern = r'[a-z]+(_[a-z]+)+'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
assert text_lowercase_underscore("aab_cbbbc") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==('Found a match!')
    assert text_lowercase_underscore("aab_Abbbc")==('Not matched!')
    assert text_lowercase_underscore("Aaab_abbbc")==('Not matched!')
