# MBPP/917
### Completion
import re

def text_uppercase_lowercase(text):
    """
    This function checks if the input string contains sequences of one uppercase letter
    followed by one or more lowercase letters.
    
    Args:
    text (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether a match was found or not.
    """
    # Regular expression pattern to match one uppercase letter followed by one or more lowercase letters
    pattern = r'[A-Z][a-z]+'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided test case
assert text_uppercase_lowercase("AaBbGg") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_uppercase_lowercase("AaBbGg")==('Found a match!')
    assert text_uppercase_lowercase("aA")==('Not matched!')
    assert text_uppercase_lowercase("PYTHON")==('Not matched!')
