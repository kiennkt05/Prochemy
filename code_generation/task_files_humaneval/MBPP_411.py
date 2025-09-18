# MBPP/411
### Completion
import re

def snake_to_camel(snake_str):
    """
    Convert a snake case string to camel case string.

    Args:
    snake_str (str): The input string in snake case.

    Returns:
    str: The converted string in camel case.
    """
    # Use regex to find underscores followed by a letter and capitalize the letter
    camel_str = re.sub(r'_(.)', lambda match: match.group(1).upper(), snake_str)
    # Capitalize the first letter of the result
    return camel_str.capitalize()

# Test case
assert snake_to_camel('android_tv') == 'AndroidTv'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'
