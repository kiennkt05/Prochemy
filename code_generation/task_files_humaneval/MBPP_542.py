# MBPP/542
### Completion
import re

def fill_spaces(input_string):
    """
    Replace all occurrences of spaces, commas, or dots in the input string with a colon.

    Parameters:
    input_string (str): The string to be modified.

    Returns:
    str: The modified string with spaces, commas, and dots replaced by colons.
    """
    # Use regex to replace spaces, commas, or dots with a colon
    modified_string = re.sub(r'[ ,.]', ':', input_string)
    return modified_string

# Test case
assert fill_spaces('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fill_spaces('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
    assert fill_spaces('Stereo Sound Sweatproof') == 'Stereo:Sound:Sweatproof'
    assert fill_spaces('Probass Curve Audio') == 'Probass:Curve:Audio'
