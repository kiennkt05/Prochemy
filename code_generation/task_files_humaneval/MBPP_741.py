# MBPP/741
### Completion
def all_Characters_Same(s: str) -> bool:
    """
    Check if all characters in the string are the same.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if all characters are the same, False otherwise.
    """
    # Check if the string is empty
    if not s:
        return True  # An empty string is considered to have all the same characters

    # Compare each character to the first character
    first_char = s[0]
    for char in s:
        if char != first_char:
            return False  # Found a different character

    return True  # All characters are the same

# Test case
assert all_Characters_Same("python") == False  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False
