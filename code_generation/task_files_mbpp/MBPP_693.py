# MBPP/693
### Completion
import re

def remove_multiple_spaces(input_string):
    # Use regex to replace multiple spaces with a single space
    return re.sub(r'\s+', ' ', input_string).strip()

# Test the function with the provided assertion
assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
    assert remove_multiple_spaces('Quad      Core') == 'Quad Core'
    assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'
