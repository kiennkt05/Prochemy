# MBPP/228
### Completion
def all_Bits_Set_In_The_Given_Range(num, start, end):
    """
    Check if all bits in the given range [start, end] are unset (0) in the binary representation of num.
    
    Parameters:
    num (int): The number to check.
    start (int): The starting bit position (1-indexed).
    end (int): The ending bit position (1-indexed).
    
    Returns:
    bool: True if all bits in the range are unset, False otherwise.
    """
    # Create a mask for the bits in the range [start, end]
    mask = ((1 << end) - 1) ^ ((1 << (start - 1)) - 1)
    
    # Check if the bits in the range are unset
    return (num & mask) == 0

# Test case
assert all_Bits_Set_In_The_Given_Range(4, 1, 2) == True  # Binary of 4 is 100, bits 1 and 2 are unset
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False
