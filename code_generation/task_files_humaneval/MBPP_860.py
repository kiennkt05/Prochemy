# MBPP/860
### Completion
import re

def check_alphanumeric(s):
    """
    Check if the given string ends with only alphanumeric characters.

    Parameters:
    s (str): The input string to check.

    Returns:
    str: 'Discard' if the string does not end with alphanumeric characters,
         'Accept' if it does.
    """
    # Regular expression to check if the string ends with alphanumeric characters
    if re.search(r'[a-zA-Z0-9]$', s):
        return 'Accept'
    else:
        return 'Discard'

# Test case
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
