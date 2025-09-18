# MBPP/7
### Completion
import re

def find_char_long(input_string):
    """
    Find all words in the input string that are at least 4 characters long.

    Args:
    input_string (str): The string to search for words.

    Returns:
    list: A list of words that are at least 4 characters long.
    """
    # Regex pattern to find words with at least 4 characters
    pattern = r'\b\w{4,}\b'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

# Test case
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
