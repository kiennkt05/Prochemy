# MBPP/879
### Completion
import re

def text_match(string):
    # Define the regex pattern
    pattern = r'a.*b$'
    
    # Use re.match to check if the pattern matches the string
    if re.match(pattern, string):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test the function
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
