# MBPP/437
### Completion
def remove_odd(s: str) -> str:
    """
    Remove characters from odd indices in the given string.

    Parameters:
    s (str): The input string from which to remove odd-indexed characters.

    Returns:
    str: A new string containing only characters from even indices.
    """
    # Using slicing to get characters at even indices
    return s[::2]

# Test case
assert remove_odd("python") == "yhn"

# Additional test cases for verification
assert remove_odd("abcdef") == "ace"
assert remove_odd("123456789") == "13579"
assert remove_odd("") == ""  # Edge case: empty string
assert remove_odd("a") == "a"  # Edge case: single character
assert remove_odd("ab") == "a"  # Edge case: two characters

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_odd("python")==("yhn")
    assert remove_odd("program")==("rga")
    assert remove_odd("language")==("agae")
