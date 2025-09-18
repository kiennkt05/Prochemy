# MBPP/194
### Completion
def octal_To_Decimal(octal):
    """
    Convert an octal number (base 8) to a decimal number (base 10).
    
    Parameters:
    octal (int): The octal number to convert.
    
    Returns:
    int: The decimal equivalent of the octal number.
    """
    decimal = 0
    power = 0
    
    # Process each digit in the octal number
    while octal > 0:
        digit = octal % 10  # Get the last digit
        decimal += digit * (8 ** power)  # Convert to decimal
        octal //= 10  # Remove the last digit
        power += 1  # Move to the next power of 8
    
    return decimal

# Test the function with the provided test case
assert octal_To_Decimal(25) == 21

# Additional test cases
assert octal_To_Decimal(10) == 8  # 1*8^1 + 0*8^0 = 8
assert octal_To_Decimal(7) == 7    # 7*8^0 = 7
assert octal_To_Decimal(17) == 15  # 1*8^1 + 7*8^0 = 8 + 7 = 15
assert octal_To_Decimal(100) == 64  # 1*8^2 + 0*8^1 + 0*8^0 = 64

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert octal_To_Decimal(25) == 21
    assert octal_To_Decimal(30) == 24
    assert octal_To_Decimal(40) == 32
