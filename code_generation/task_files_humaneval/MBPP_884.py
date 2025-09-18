# MBPP/884
### Completion
def all_Bits_Set_In_The_Given_Range(n, start, end):
    """
    Check if all bits in the range [start, end] are set to 1 in the binary representation of n.

    Parameters:
    n (int): The integer to check.
    start (int): The starting bit position (0-indexed).
    end (int): The ending bit position (0-indexed).

    Returns:
    bool: True if all bits in the range are set to 1, False otherwise.
    """
    # Create a mask with bits set to 1 in the range [start, end]
    mask = ((1 << (end - start + 1)) - 1) << start
    
    # Check if the bits in the range are set in n
    return (n & mask) == mask

# Test case
assert all_Bits_Set_In_The_Given_Range(10, 2, 1) == True  # 10 in binary is 1010, bits 1 and 2 are set
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(10,2,1) == True 
    assert all_Bits_Set_In_The_Given_Range(5,2,4) == False
    assert all_Bits_Set_In_The_Given_Range(22,2,3) == True 
