# MBPP/269
### Completion
def ascii_value(char):
    """
    Returns the ASCII value of a given character.

    Parameters:
    char (str): A single character whose ASCII value is to be found.

    Returns:
    int: The ASCII value of the character.
    
    Raises:
    ValueError: If the input is not a single character.
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    
    return ord(char)

# Test case
assert ascii_value('A') == 65
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ascii_value('A')==65
    assert ascii_value('R')==82
    assert ascii_value('S')==83
