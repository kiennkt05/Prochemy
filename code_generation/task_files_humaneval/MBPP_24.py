# MBPP/24
### Completion
def binary_to_decimal(binary):
    """
    Convert a binary number (given as an integer) to its decimal equivalent.

    Parameters:
    binary (int): The binary number to convert.

    Returns:
    int: The decimal equivalent of the binary number.
    """
    # Convert the binary number to a string to process each digit
    binary_str = str(binary)
    decimal_value = 0
    
    # Iterate over each digit in the binary string
    for index, digit in enumerate(reversed(binary_str)):
        # Convert the character to an integer and calculate its decimal value
        decimal_value += int(digit) * (2 ** index)
    
    return decimal_value

# Test case
assert binary_to_decimal(100) == 4  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_to_decimal(100) == 4
    assert binary_to_decimal(1011) == 11
    assert binary_to_decimal(1101101) == 109
