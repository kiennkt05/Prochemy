# MBPP/451
### Completion
import re

def remove_whitespaces(input_string):
    # Use regex to replace all whitespace characters with an empty string
    return re.sub(r'\s+', '', input_string)

# Test the function with the provided assertion
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
