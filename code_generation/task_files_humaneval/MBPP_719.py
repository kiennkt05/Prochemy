# MBPP/719
### Completion
import re

def text_match(string):
    """
    This function checks if the input string contains an 'a' followed by zero or more 'b's.
    
    Parameters:
    string (str): The input string to be checked.
    
    Returns:
    str: A message indicating whether a match was found or not.
    """
    # Regular expression pattern to match 'a' followed by zero or more 'b's
    pattern = r'a(b*)'
    
    # Use re.fullmatch to check if the entire string matches the pattern
    if re.fullmatch(pattern, string):
        return 'Found a match!'
    else:
        return 'No match found.'

# Test case
assert text_match("ac") == 'No match found.'  # "ac" does not match the pattern
assert text_match("a") == 'Found a match!'    # "a" matches the pattern
assert text_match("ab") == 'Found a match!'   # "ab" matches the pattern
assert text_match("abb") == 'Found a match!'  # "abb" matches the pattern
assert text_match("b") == 'No match found.'    # "b" does not match the pattern
assert text_match("") == 'No match found.'      # Empty string does not match the pattern

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match("ac")==('Found a match!')
    assert text_match("dc")==('Not matched!')
    assert text_match("abba")==('Found a match!')
