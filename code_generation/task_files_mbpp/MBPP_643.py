# MBPP/643
### Completion
import re

def text_match_wordz_middle(text):
    # Regular expression to find a word containing 'z' not at the start or end
    pattern = r'\b\w*z\w*\b'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function
assert text_match_wordz_middle("pythonzabc.") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_wordz_middle("pythonzabc.")==('Found a match!')
    assert text_match_wordz_middle("xyzabc.")==('Found a match!')
    assert text_match_wordz_middle("  lang  .")==('Not matched!')
