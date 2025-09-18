# MBPP/186
### Completion
import re

def check_literals(input_string, literals):
    """
    Check if any of the literal strings are present in the input string using regex.

    Parameters:
    input_string (str): The string to search within.
    literals (list): A list of literal strings to search for.

    Returns:
    str: 'Matched!' if any literal is found, 'Not Matched!' otherwise.
    """
    # Iterate through each literal in the list
    for literal in literals:
        # Use regex to search for the literal in the input string
        if re.search(re.escape(literal), input_string):
            return 'Matched!'
    
    return 'Not Matched!'

# Test case
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
