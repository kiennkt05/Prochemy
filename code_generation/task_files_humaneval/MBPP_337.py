# MBPP/337
### Completion
import re

def text_match_word(text):
    """
    Check if the input text ends with the word 'python' followed by optional punctuation.
    
    Args:
    text (str): The input string to check.
    
    Returns:
    str: A message indicating whether a match was found.
    """
    # Define the regex pattern to match 'python' at the end of the string with optional punctuation
    pattern = r'python[.,!?;:]?$'
    
    # Use re.search to find a match
    if re.search(pattern, text, re.IGNORECASE):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test the function with the provided test case
assert text_match_word("python.") == 'Found a match!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_word("python.")==('Found a match!')
    assert text_match_word("python.")==('Found a match!')
    assert text_match_word("  lang  .")==('Not matched!')
