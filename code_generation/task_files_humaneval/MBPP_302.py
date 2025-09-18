# MBPP/302
### Completion
def set_Bit_Number(n):
    """
    This function returns the value of the most significant bit that is set in the binary representation of n.
    
    Parameters:
    n (int): The input integer to find the most significant set bit.
    
    Returns:
    int: The value of the most significant bit that is set.
    """
    if n <= 0:
        return 0  # If n is 0 or negative, there are no set bits.
    
    msb_value = 1  # Start with the least significant bit value.
    
    # Shift left until we find the most significant bit
    while n > 1:
        n >>= 1  # Right shift n to check the next bit
        msb_value <<= 1  # Move to the next bit value
    
    return msb_value

# Test case
assert set_Bit_Number(6) == 4  # The binary representation of 6 is '110', MSB is 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_Bit_Number(6) == 4
    assert set_Bit_Number(10) == 8
    assert set_Bit_Number(18) == 16
