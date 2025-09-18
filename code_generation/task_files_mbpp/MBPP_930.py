# MBPP/930
### Completion
import re

def text_match(string):
    # Define the regex pattern for 'a' followed by zero or more 'b's
    pattern = r'a(b*)'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, string):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test the function
assert text_match("msb") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match("msb") == 'Not matched!'
    assert text_match("a0c") == 'Found a match!'
    assert text_match("abbc") == 'Found a match!'
