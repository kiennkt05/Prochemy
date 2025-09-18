# MBPP/16
### Completion
import re

def text_lowercase_underscore(text):
    # Regular expression to find sequences of lowercase letters joined with an underscore
    pattern = r'^[a-z]+(_[a-z]+)*$'
    
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided assertion
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
