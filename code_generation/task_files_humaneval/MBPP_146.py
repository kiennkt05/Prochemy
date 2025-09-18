# MBPP/146
### Completion
def ascii_value_string(s: str) -> int:
    """
    Calculate the ASCII value of the total number of characters in the input string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The ASCII value of the total character count.
    """
    # Calculate the total number of characters in the string
    total_characters = len(s)
    
    # Convert the total character count to string and get its ASCII value
    ascii_value = ord(str(total_characters))
    
    return ascii_value

# Test case
assert ascii_value_string("python") == 112  # The length of "python" is 6, and ord('6') is 54
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ascii_value_string("python")==112
    assert ascii_value_string("Program")==80
    assert ascii_value_string("Language")==76
