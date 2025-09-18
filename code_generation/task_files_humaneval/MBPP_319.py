# MBPP/319
### Completion
import re

def find_long_word(input_string):
    """
    Find all five-character long words in the given string using regex.

    Args:
    input_string (str): The string to search for five-character words.

    Returns:
    list: A list of five-character long words found in the input string.
    """
    # Regex pattern to find words that are exactly five characters long
    pattern = r'\b\w{5}\b'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

# Test case
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
