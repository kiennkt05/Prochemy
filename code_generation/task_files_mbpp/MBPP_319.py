# MBPP/319
### Completion
import re

def find_long_word(input_string):
    # Use regex to find all words that are exactly 5 characters long
    return re.findall(r'\b\w{5}\b', input_string)

# Test the function with the provided assertion
assert find_long_word('Please move back to strem') == ['strem']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_long_word('Please move back to strem') == ['strem']
    assert find_long_word('4K Ultra HD streaming player') == ['Ultra']
    assert find_long_word('Streaming Media Player') == ['Media']
