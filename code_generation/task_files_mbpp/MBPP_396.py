# MBPP/396
### Completion
import re

def check_char(s):
    # Use regex to check if the first and last character are the same
    if re.match(r'^(?P<first>.)(?P=first).*?(?P=first)$', s):
        return "Valid"
    else:
        return "Invalid"

# Test the function
assert check_char("abba") == "Valid"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"
