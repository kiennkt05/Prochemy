# MBPP/868
### Completion
def length_of_last_word(s: str) -> int:
    """
    Returns the length of the last word in the given string.
    
    Parameters:
    s (str): The input string from which to find the last word.
    
    Returns:
    int: The length of the last word.
    """
    # Strip the string to remove leading and trailing whitespace
    s = s.strip()
    
    # Split the string into words
    words = s.split()
    
    # Check if there are any words in the list
    if not words:
        return 0  # Return 0 if there are no words
    
    # Get the last word
    last_word = words[-1]
    
    # Return the length of the last word
    return len(last_word)

# Test case
assert length_of_last_word("python language") == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert length_Of_Last_Word("python language") == 8
    assert length_Of_Last_Word("PHP") == 3
    assert length_Of_Last_Word("") == 0
