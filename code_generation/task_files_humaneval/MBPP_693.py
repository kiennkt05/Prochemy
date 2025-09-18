# MBPP/693
### Completion
import re

def remove_multiple_spaces(input_string):
    """
    Remove multiple spaces from the input string and replace them with a single space.

    Parameters:
    input_string (str): The string from which to remove multiple spaces.

    Returns:
    str: The modified string with single spaces.
    """
    # Use regex to replace multiple spaces with a single space
    return re.sub(r'\s+', ' ', input_string).strip()

# Test case
assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'

# Additional test cases
assert remove_multiple_spaces('   Hello   World!   ') == 'Hello World!'
assert remove_multiple_spaces('This   is   a   test.') == 'This is a test.'
assert remove_multiple_spaces('NoSpacesHere') == 'NoSpacesHere'
assert remove_multiple_spaces('   Leading and trailing spaces   ') == 'Leading and trailing spaces'
assert remove_multiple_spaces('Multiple    spaces    in between') == 'Multiple spaces in between'

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
    assert remove_multiple_spaces('Quad      Core') == 'Quad Core'
    assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'
