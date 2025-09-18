# MBPP/224
### Completion
def count_Set_Bits(n):
    """
    Count the number of set bits (1s) in the binary representation of a given number.

    Parameters:
    n (int): The number for which to count the set bits.

    Returns:
    int: The count of set bits in the binary representation of n.
    """
    count = 0  # Initialize count of set bits
    while n > 0:
        count += n & 1  # Increment count if the least significant bit is 1
        n >>= 1  # Right shift n to check the next bit
    return count

# Test case
assert count_Set_Bits(2) == 1  # Binary representation of 2 is '10', which has 1 set bit.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2
