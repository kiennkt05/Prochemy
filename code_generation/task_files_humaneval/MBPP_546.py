# MBPP/546
### Completion
def last_occurrence_char(s: str, char: str) -> int:
    """
    Find the last occurrence of a character in a string.

    Parameters:
    s (str): The string to search within.
    char (str): The character to find.

    Returns:
    int: The index of the last occurrence of the character, or -1 if not found.
    """
    # Use rfind to get the last occurrence of the character
    return s.rfind(char)

# Test case
assert last_occurrence_char("hello world", 'l') == 10

# Additional test cases for verification
assert last_occurrence_char("hello world", 'o') == 7
assert last_occurrence_char("hello world", 'h') == 0
assert last_occurrence_char("hello world", 'z') == -1
assert last_occurrence_char("", 'a') == -1  # Edge case: empty string
assert last_occurrence_char("abcabcabc", 'a') == 6  # Last 'a' in the string
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_occurence_char("hello world",'l')==10
    assert last_occurence_char("language",'g')==7
    assert last_occurence_char("little",'y')==None
