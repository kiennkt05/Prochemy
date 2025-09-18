# MBPP/461
### Completion
def upper_ctr(s: str) -> int:
    """
    Count the number of uppercase characters in a given string.

    Parameters:
    s (str): The input string to be analyzed.

    Returns:
    int: The count of uppercase characters in the string.
    """
    count = 0  # Initialize the counter for uppercase characters
    for char in s:  # Iterate through each character in the string
        if char.isupper():  # Check if the character is uppercase
            count += 1  # Increment the counter if it is uppercase
    return count  # Return the final count

# Test case
assert upper_ctr('PYthon') == 1  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0
