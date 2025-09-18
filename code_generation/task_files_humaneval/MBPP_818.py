# MBPP/818
### Completion
def lower_ctr(s: str) -> int:
    """
    Count the number of lowercase letters in the given string.

    Parameters:
    s (str): The input string to be analyzed.

    Returns:
    int: The count of lowercase letters in the string.
    """
    count = 0  # Initialize the counter for lowercase letters
    for char in s:  # Iterate through each character in the string
        if char.islower():  # Check if the character is a lowercase letter
            count += 1  # Increment the counter if it is lowercase
    return count  # Return the final count

# Test case
assert lower_ctr('abc') == 3  # This should pass as there are 3 lowercase letters
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lower_ctr('abc') == 3
    assert lower_ctr('string') == 6
    assert lower_ctr('Python') == 5
