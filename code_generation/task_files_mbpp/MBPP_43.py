# MBPP/43
### Completion
import re

def text_match(text):
    # Define the regex pattern to match sequences of lowercase letters joined with an underscore
    pattern = r'^[a-z]+(_[a-z]+)*$'
    
    # Use re.match to check if the entire string matches the pattern
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided assertion
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
