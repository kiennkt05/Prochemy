# MBPP/607
### Completion
import re

def find_literals(original_string, pattern):
    # Use re.search to find the pattern in the original string
    match = re.search(re.escape(pattern), original_string)
    
    if match:
        # If a match is found, return the matched string and its start and end positions
        return (match.group(0), match.start(), match.end())
    else:
        # If no match is found, return None or an appropriate value
        return None

# Example usage
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
