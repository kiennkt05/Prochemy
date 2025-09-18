# MBPP/917
### Completion
import re

def text_uppercase_lowercase(text):
    # Regular expression to match one uppercase letter followed by one or more lowercase letters
    pattern = r'[A-Z][a-z]+'
    
    # Find all matches in the input text
    matches = re.findall(pattern, text)
    
    # Check if any matches were found
    if matches:
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided assertion
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
