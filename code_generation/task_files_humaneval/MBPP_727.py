# MBPP/727
### Completion
import re

def remove_char(input_string):
    """
    Remove all characters from the input string except letters and numbers.

    Args:
    input_string (str): The string from which to remove unwanted characters.

    Returns:
    str: A string containing only letters and numbers.
    """
    # Use regex to substitute all non-alphanumeric characters with an empty string
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    return cleaned_string

# Test case
assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'
    assert remove_char("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'
    assert remove_char("Cool543Triks@:, Make@987Trips") == 'Cool543TriksMake987Trips' 
