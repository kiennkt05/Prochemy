# MBPP/631
### Completion
import re

def replace_spaces(input_string):
    """
    Replace whitespaces with underscores and vice versa in the given string.

    Parameters:
    input_string (str): The string to be modified.

    Returns:
    str: The modified string with whitespaces and underscores swapped.
    """
    # Replace spaces with a temporary placeholder
    temp_string = re.sub(r'\s+', '_', input_string)  # Replace spaces with underscores
    # Replace underscores with spaces
    result_string = re.sub(r'_', ' ', temp_string)  # Replace underscores with spaces
    return result_string

# Test case
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The Avengers') == 'The_Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'
