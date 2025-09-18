# MBPP/957
### Completion
def get_First_Set_Bit_Pos(n):
    """
    Returns the position of the rightmost set bit in the binary representation of n.
    
    Parameters:
    n (int): The integer to check.
    
    Returns:
    int: The position of the rightmost set bit (1-indexed).
    """
    if n == 0:
        return 0  # If n is 0, there are no set bits.
    
    # Isolate the rightmost set bit
    rightmost_set_bit = n & -n
    
    # Find the position of the rightmost set bit
    position = 1  # Start counting from position 1
    while rightmost_set_bit > 1:
        rightmost_set_bit >>= 1  # Right shift to check the next bit
        position += 1  # Increment position
    
    return position

# Test case
assert get_First_Set_Bit_Pos(12) == 3  # Binary of 12 is 1100, rightmost set bit is at position 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_First_Set_Bit_Pos(12) == 3
    assert get_First_Set_Bit_Pos(18) == 2
    assert get_First_Set_Bit_Pos(16) == 5
