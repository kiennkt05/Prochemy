# MBPP/482
### Completion
import re

def match(s):
    # Define the regex pattern for one uppercase letter followed by lowercase letters
    pattern = r'^[A-Z][a-z]*$'
    
    # Use re.match to check if the entire string matches the pattern
    if re.match(pattern, s):
        return 'Yes'
    else:
        return 'No'

# Test the function with the provided assertion
assert match("Geeks") == 'Yes'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert match("Geeks") == 'Yes'
    assert match("geeksforGeeks") == 'Yes'
    assert match("geeks") == 'No'
