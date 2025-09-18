# MBPP/395
### Completion
def first_non_repeating_character(s: str) -> str:
    """
    Find the first non-repeated character in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The first non-repeated character or None if all characters are repeated.
    """
    # Dictionary to count occurrences of each character
    char_count = {}

    # Count each character in the string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char

    # If no non-repeated character is found, return None
    return None

# Test case
assert first_non_repeating_character("abcabc") == None
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"
