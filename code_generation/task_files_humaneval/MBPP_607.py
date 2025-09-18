# MBPP/607
### Completion
import re

def find_literals(original_string, literal_string):
    """
    Searches for a literal string within the original string and returns
    the matched string along with its start and end indices.

    Parameters:
    original_string (str): The string to search within.
    literal_string (str): The literal string to search for.

    Returns:
    tuple: A tuple containing the matched string and its start and end indices,
           or None if no match is found.
    """
    # Use re.search to find the first occurrence of the literal string
    match = re.search(re.escape(literal_string), original_string)
    
    if match:
        # If a match is found, return the matched string and its indices
        start_index = match.start()
        end_index = match.end()
        return (match.group(), start_index, end_index)
    
    # Return None if no match is found
    return None

# Test case
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)
