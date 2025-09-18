# MBPP/352
### Completion
def unique_characters(s: str) -> bool:
    """
    Check if all characters in the given string are unique.

    Parameters:
    s (str): The input string to check for unique characters.

    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    seen = set()  # Set to keep track of seen characters
    for char in s:
        if char in seen:
            return False  # Duplicate character found
        seen.add(char)  # Add character to the set
    return True  # All characters are unique

# Test cases
assert unique_characters('aba') == False  # Example test case
assert unique_characters('abc') == True    # All characters are unique
assert unique_characters('') == True       # Empty string has unique characters
assert unique_characters('a') == True      # Single character is unique
assert unique_characters('abcdefg') == True # All characters are unique
assert unique_characters('aabbcc') == False # Duplicate characters present

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_Characters('aba') == False
    assert unique_Characters('abc') == True
    assert unique_Characters('abab') == False
