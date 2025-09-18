# MBPP/11
### Completion
def remove_Occ(s: str, char: str) -> str:
    """
    Remove the first and last occurrence of a given character from the string.

    Parameters:
    s (str): The input string from which to remove characters.
    char (str): The character to remove from the string.

    Returns:
    str: The modified string with the first and last occurrence of the character removed.
    """
    # Find the first occurrence of the character
    first_index = s.find(char)
    # Find the last occurrence of the character
    last_index = s.rfind(char)

    # If the character is not found or only one occurrence exists, return the original string
    if first_index == -1 or first_index == last_index:
        return s.replace(char, '', 1)  # Remove only the first occurrence if it's the same

    # Create a new string without the first and last occurrence of the character
    new_string = s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
    
    return new_string

# Test case
assert remove_Occ("hello", "l") == "heo"

# Additional test cases
assert remove_Occ("banana", "a") == "bnna"  # Remove first and last 'a'
assert remove_Occ("apple", "p") == "ale"    # Remove first and last 'p'
assert remove_Occ("test", "t") == "es"      # Remove first and last 't'
assert remove_Occ("hello", "x") == "hello"  # Character not found, return original
assert remove_Occ("a", "a") == ""            # Only one occurrence, should return empty string

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_Occ("hello","l") == "heo"
    assert remove_Occ("abcda","a") == "bcd"
    assert remove_Occ("PHP","P") == "H"
