# MBPP/478
### Completion
def remove_lowercase(s: str) -> str:
    """
    Remove all lowercase substrings from the given string.

    Parameters:
    s (str): The input string from which lowercase substrings will be removed.

    Returns:
    str: A new string with all lowercase characters removed.
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            result += char  # Append uppercase characters to the result
    
    return result

# Test the function with the provided test case
assert remove_lowercase("PYTHon") == 'PYTH'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')
