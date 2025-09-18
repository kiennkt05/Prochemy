# MBPP/643
### Completion
import re

def text_match_wordz_middle(text):
    """
    This function checks if there is a word in the given text that contains the letter 'z'
    not at the start or end of the word.
    
    Args:
    text (str): The input string to search for the pattern.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Regular expression to find 'z' not at the start or end of a word
    pattern = r'\b\w*z\w*\b'
    
    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
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
