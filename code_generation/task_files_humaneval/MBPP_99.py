# MBPP/99
### Completion
def decimal_to_binary(n):
    """
    Convert a decimal number to its binary equivalent.

    Parameters:
    n (int): The decimal number to convert.

    Returns:
    str: The binary representation of the decimal number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Special case for 0
    if n == 0:
        return '0'
    
    binary_digits = []
    
    # Convert decimal to binary
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n //= 2
    
    # The binary digits are in reverse order, so we reverse them
    binary_digits.reverse()
    
    return ''.join(binary_digits)

# Test the function with the provided test case
assert decimal_to_binary(8) == '1000'

# Additional test cases
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(5) == '101'
assert decimal_to_binary(10) == '1010'

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111' 
