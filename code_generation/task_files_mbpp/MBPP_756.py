# MBPP/756
### Completion
import re

def text_match_zero_one(text):
    # Regular expression to match 'a' followed by zero or one 'b'
    pattern = r'a(b)?'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided assertion
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
