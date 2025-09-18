# MBPP/186
### Completion
import re

def check_literals(input_string, literals):
    # Create a regex pattern that matches any of the literals
    pattern = '|'.join(map(re.escape, literals))
    
    # Search for the pattern in the input string
    if re.search(pattern, input_string):
        return 'Matched!'
    else:
        return 'Not Matched!'

# Example usage
assert check_literals('The quick brown fox jumps over the lazy dog.', ['fox']) == 'Matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_literals('The quick brown fox jumps over the lazy dog.',['fox']) == 'Matched!'
    assert check_literals('The quick brown fox jumps over the lazy dog.',['horse']) == 'Not Matched!'
    assert check_literals('The quick brown fox jumps over the lazy dog.',['lazy']) == 'Matched!'
