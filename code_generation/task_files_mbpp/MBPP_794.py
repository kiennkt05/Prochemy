# MBPP/794
### Completion
import re

def text_starta_endb(text):
    # Regular expression to match 'a' followed by anything and ending with 'b'
    pattern = r'^a.*b$'
    
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided assertion
assert text_starta_endb("aabbbb") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_starta_endb("aabbbb")==('Found a match!')
    assert text_starta_endb("aabAbbbc")==('Not matched!')
    assert text_starta_endb("accddbbjjj")==('Not matched!')
