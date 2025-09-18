# MBPP/454
### Completion
import re

def text_match_wordz(text):
    """
    This function checks if the input text contains any word with the letter 'z'.
    
    Parameters:
    text (str): The input string to search for words containing 'z'.
    
    Returns:
    str: A message indicating whether a match was found or not.
    """
    # Regular expression to find words containing 'z'
    if re.search(r'\b\w*z\w*\b', text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
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
