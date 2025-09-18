# MBPP/217
### Completion
def first_repeated_char(s: str) -> str:
    """
    Function to find the first repeated character in a given string.
    
    Parameters:
    s (str): The input string to search for repeated characters.
    
    Returns:
    str: The first repeated character, or None if no character is repeated.
    """
    seen = set()  # Set to keep track of seen characters
    
    for char in s:
        if char in seen:
            return char  # Return the first repeated character
        seen.add(char)  # Add the character to the set if not seen
    
    return None  # Return None if no repeated character is found

# Test case
assert first_repeated_char("Google") == "o"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Repeated_Char("Google") == "o"
    assert first_Repeated_Char("data") == "a"
    assert first_Repeated_Char("python") == '\0'
