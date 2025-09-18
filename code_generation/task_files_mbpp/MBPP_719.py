# MBPP/719
### Completion
import re

def text_match(text):
    # Define the regex pattern for 'a' followed by zero or more 'b's
    pattern = r'a(b*)'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function
assert text_match("ac") == 'No match found.'
assert text_match("ab") == 'Found a match!'
assert text_match("a") == 'Found a match!'
assert text_match("abb") == 'Found a match!'
assert text_match("abc") == 'No match found.'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match("ac")==('Found a match!')
    assert text_match("dc")==('Not matched!')
    assert text_match("abba")==('Found a match!')
