# MBPP/44
### Completion
def text_match_string(text):
    """
    Check if the input string starts with the word 'python'.
    
    Parameters:
    text (str): The input string to check.
    
    Returns:
    str: A message indicating whether the string starts with 'python'.
    """
    # Check if the string starts with 'python'
    if text.startswith("python"):
        return "Matched!"
    else:
        return "Not matched!"

# Test case
assert text_match_string(" python") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_string(" python")==('Not matched!')
    assert text_match_string("python")==('Found a match!')
    assert text_match_string("  lang")==('Not matched!')
