# MBPP/454
### Completion
import re

def text_match_wordz(text):
    # Use regex to search for a word containing 'z'
    if re.search(r'\b\w*z\w*\b', text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function
assert text_match_wordz("pythonz.") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_wordz("pythonz.")==('Found a match!')
    assert text_match_wordz("xyz.")==('Found a match!')
    assert text_match_wordz("  lang  .")==('Not matched!')
