# MBPP/666
### Completion
def count_char(s: str, char: str) -> int:
    """
    Count the occurrences of a character in a string.

    Parameters:
    s (str): The string in which to count occurrences.
    char (str): The character to count in the string.

    Returns:
    int: The number of occurrences of the character in the string.
    """
    # Ensure that char is a single character
    if len(char) != 1:
        raise ValueError("The 'char' parameter must be a single character.")
    
    # Use the count method to count occurrences of char in s
    return s.count(char)

# Test case
assert count_char("Python", 'o') == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_char("Python",'o')==1
    assert count_char("little",'t')==2
    assert count_char("assert",'s')==2
