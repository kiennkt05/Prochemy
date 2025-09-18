# MBPP/480
### Completion
from collections import Counter

def get_max_occuring_char(s: str) -> str:
    """
    Function to find the maximum occurring character in a given string.
    
    Parameters:
    s (str): The input string from which to find the maximum occurring character.
    
    Returns:
    str: The character that occurs the most in the string. 
         In case of a tie, the first character encountered with the maximum count is returned.
    """
    # Count the occurrences of each character in the string
    char_count = Counter(s)
    
    # Find the character with the maximum count
    max_char = max(char_count, key=lambda char: (char_count[char], char))
    
    return max_char

# Test case
assert get_max_occuring_char("data") == "a"

# Additional test cases for verification
assert get_max_occuring_char("hello") == "l"
assert get_max_occuring_char("character") == "c"
assert get_max_occuring_char("aabbcc") == "a"  # In case of tie, 'a' comes first
assert get_max_occuring_char("") == ""  # Edge case: empty string
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_max_occuring_char("data") == "a"
    assert get_max_occuring_char("create") == "e"
    assert get_max_occuring_char("brilliant girl") == "i"
