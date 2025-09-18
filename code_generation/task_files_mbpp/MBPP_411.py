# MBPP/411
### Completion
import re

def snake_to_camel(snake_str):
    # Use regex to find all occurrences of words separated by underscores
    components = re.split(r'_', snake_str)
    # Capitalize the first letter of each component and join them
    return ''.join(x.capitalize() for x in components)

# Test the function
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
