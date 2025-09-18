# MBPP/671
### Completion
def set_Right_most_Unset_Bit(n):
    """
    Set the rightmost unset bit of the given integer n.
    
    Parameters:
    n (int): The integer whose rightmost unset bit is to be set.
    
    Returns:
    int: The integer after setting the rightmost unset bit.
    """
    # Find the rightmost unset bit
    # We can use the expression n + 1 to find the rightmost unset bit
    # The expression n & -n gives us the rightmost set bit
    # We can use the bitwise NOT to find the rightmost unset bit
    return n | (n + 1)

# Test the function with the provided test case
assert set_Right_most_Unset_Bit(21) == 23

# Additional test cases
assert set_Right_most_Unset_Bit(0) == 1  # 0 in binary is 0000, setting the rightmost unset bit gives 0001
assert set_Right_most_Unset_Bit(1) == 3  # 1 in binary is 0001, setting the rightmost unset bit gives 0011
assert set_Right_most_Unset_Bit(2) == 3  # 2 in binary is 0010, setting the rightmost unset bit gives 0011
assert set_Right_most_Unset_Bit(3) == 7  # 3 in binary is 0011, setting the rightmost unset bit gives 0111

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_Right_most_Unset_Bit(21) == 23
    assert set_Right_most_Unset_Bit(11) == 15
    assert set_Right_most_Unset_Bit(15) == 15
