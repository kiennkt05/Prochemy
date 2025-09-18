# MBPP/83
### Completion
def get_Char(s: str) -> str:
    """
    This function takes a string and returns a character that is the result of
    adding the ASCII values of all characters in the string.
    
    Parameters:
    s (str): The input string from which to calculate the character.
    
    Returns:
    str: The resulting character after summing the ASCII values.
    """
    # Calculate the sum of ASCII values of all characters in the string
    ascii_sum = sum(ord(char) for char in s)
    
    # Convert the sum back to a character using modulo 256
    result_char = chr(ascii_sum % 256)
    
    return result_char

# Test case
assert get_Char("abc") == "f"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"
