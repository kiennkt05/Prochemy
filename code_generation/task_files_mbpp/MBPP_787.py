# MBPP/787
### Completion
import re

def text_match_three(text):
    # Define the regex pattern to match 'a' followed by three 'b's
    pattern = r'a(b{3})'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, text):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test the function with the provided assertion
assert text_match_three("ac") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_three("ac")==('Not matched!')
    assert text_match_three("dc")==('Not matched!')
    assert text_match_three("abbbba")==('Found a match!')
