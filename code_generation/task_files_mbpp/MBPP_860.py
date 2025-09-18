# MBPP/860
### Completion
import re

def check_alphanumeric(s):
    # Check if the string ends with only alphanumeric characters
    if re.search(r'[^\w]$', s):
        return 'Discard'
    return 'Accept'

# Test the function with the provided assertion
assert check_alphanumeric("dawood@") == 'Discard'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_alphanumeric("dawood@") == 'Discard'
    assert check_alphanumeric("skdmsam326") == 'Accept'
    assert check_alphanumeric("cooltricks@") == 'Discard'
