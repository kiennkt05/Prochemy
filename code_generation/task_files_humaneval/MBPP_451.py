# MBPP/451
### Completion
import re

def remove_whitespaces(input_string):
    """
    Remove all whitespaces from the given string using regex.

    Parameters:
    input_string (str): The string from which to remove whitespaces.

    Returns:
    str: The input string without any whitespaces.
    """
    # Use regex to substitute all whitespace characters with an empty string
    return re.sub(r'\s+', '', input_string)

# Test case
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
