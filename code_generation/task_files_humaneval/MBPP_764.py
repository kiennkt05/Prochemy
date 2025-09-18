# MBPP/764
### Completion
def number_ctr(input_string):
    """
    Count the number of numeric characters in the given string.

    Parameters:
    input_string (str): The string to be analyzed.

    Returns:
    int: The count of numeric characters in the string.
    """
    count = 0  # Initialize counter for numeric characters
    for char in input_string:  # Iterate through each character in the string
        if char.isdigit():  # Check if the character is a digit
            count += 1  # Increment the counter if it is a digit
    return count  # Return the total count of numeric characters

# Test case
assert number_ctr('program2bedone') == 1  # This should pass as there is one numeric character '2'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') ==1
    assert number_ctr('123') == 3
