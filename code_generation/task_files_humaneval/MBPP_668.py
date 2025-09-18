# MBPP/668
### Completion
import re

def replace(input_string, char_to_replace):
    """
    Replace multiple occurrences of a specified character in a string with a single occurrence.

    Parameters:
    input_string (str): The string in which to replace characters.
    char_to_replace (str): The character to be replaced.

    Returns:
    str: The modified string with multiple occurrences replaced by a single occurrence.
    """
    # Use regular expression to replace multiple occurrences of char_to_replace with a single one
    pattern = f"{re.escape(char_to_replace)}+"
    modified_string = re.sub(pattern, char_to_replace, input_string)
    return modified_string

# Test case
assert replace('peep', 'e') == 'pep'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace('peep','e') == 'pep'
    assert replace('Greek','e') == 'Grek'
    assert replace('Moon','o') == 'Mon'
