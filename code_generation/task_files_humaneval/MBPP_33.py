# MBPP/33
### Completion
def decimal_to_binary(decimal_number):
    """
    Convert a decimal number to its binary representation.

    Parameters:
    decimal_number (int): The decimal number to convert.

    Returns:
    str: The binary representation of the decimal number.
    """
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Convert to binary and remove the '0b' prefix
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

# Test case
assert decimal_to_binary(10) == '1010', "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decimal_To_Binary(10) == 1010
    assert decimal_To_Binary(1) == 1
    assert decimal_To_Binary(20) == 10100
