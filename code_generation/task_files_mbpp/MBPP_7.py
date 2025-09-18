# MBPP/7
### Completion
import re

def find_char_long(input_string):
    # Use regex to find all words with at least 4 characters
    return re.findall(r'\b\w{4,}\b', input_string)

# Test the function with the provided assertion
assert find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']
    assert find_char_long('Jing Eco and Tech') == ['Jing', 'Tech']
    assert find_char_long('Jhingai wulu road Zone 3') == ['Jhingai', 'wulu', 'road', 'Zone']
