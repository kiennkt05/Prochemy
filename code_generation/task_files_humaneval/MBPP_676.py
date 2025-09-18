# MBPP/676
### Completion
import re

def remove_extra_char(input_string):
    """
    Remove everything except alphanumeric characters from the given string.

    Args:
    input_string (str): The string from which to remove non-alphanumeric characters.

    Returns:
    str: A string containing only alphanumeric characters.
    """
    # Use regex to substitute non-alphanumeric characters with an empty string
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    return cleaned_string

# Test case
assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'

# You can add more test cases to validate the function
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'
    assert remove_extra_char('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'
    assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'
