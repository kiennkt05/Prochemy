# MBPP/737
### Completion
import re

def check_str(s):
    # Check if the string starts with a vowel (case insensitive)
    if re.match(r'^[aeiouAEIOU]', s):
        return 'Valid'
    else:
        return 'Invalid'

# Test the function
assert check_str("annie") == 'Valid'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_str("annie") == 'Valid'
    assert check_str("dawood") == 'Invalid'
    assert check_str("Else") == 'Valid'
