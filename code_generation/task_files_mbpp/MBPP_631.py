# MBPP/631
### Completion
import re

def replace_spaces(input_string):
    # Replace spaces with underscores and underscores with spaces
    return re.sub(r'_', ' ', re.sub(r'\s+', '_', input_string))

# Test the function with the provided assertion
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
