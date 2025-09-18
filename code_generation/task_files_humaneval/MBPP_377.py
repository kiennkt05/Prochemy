# MBPP/377
### Completion
def remove_Char(input_string: str, char_to_remove: str) -> str:
    """
    Remove all occurrences of a specified character from the input string.

    Parameters:
    input_string (str): The string from which to remove the character.
    char_to_remove (str): The character to remove from the string.

    Returns:
    str: The modified string with the specified character removed.
    """
    # Use the replace method to remove all occurrences of char_to_remove
    return input_string.replace(char_to_remove, '')

# Test case
assert remove_Char("aba", 'a') == "b"

# Additional test cases for verification
assert remove_Char("hello world", 'o') == "hell wrld"
assert remove_Char("test case", 't') == "es case"
assert remove_Char("remove all", 'a') == "remove ll"
assert remove_Char("", 'a') == ""  # Edge case: empty string
assert remove_Char("character", 'c') == "harater"  # Case sensitivity test

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_Char("aba",'a') == "b"
    assert remove_Char("toggle",'g') == "tole"
    assert remove_Char("aabbc",'b') == "aac"
