# MBPP/285
### Completion
import re

def text_match_two_three(s):
    # Define the regex pattern for 'a' followed by two to three 'b's
    pattern = r'a(b{2,3})$'
    
    # Use re.match to check if the string matches the pattern
    if re.match(pattern, s):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test the function with the provided assertion
assert text_match_two_three("ac") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_two_three("ac")==('Not matched!')
    assert text_match_two_three("dc")==('Not matched!')
    assert text_match_two_three("abbbba")==('Found a match!')
