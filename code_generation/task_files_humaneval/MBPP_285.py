# MBPP/285
### Completion
import re

def text_match_two_three(s):
    """
    This function checks if the input string matches the pattern of 'a' followed by 
    two to three 'b's. It returns a success message if matched, otherwise returns 
    'Not matched!'.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether the string matched the pattern or not.
    """
    # Define the regex pattern for 'a' followed by two to three 'b's
    pattern = r'^ab{2,3}$'
    
    # Check if the input string matches the pattern
    if re.match(pattern, s):
        return 'Matched!'
    else:
        return 'Not matched!'

# Test case
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
