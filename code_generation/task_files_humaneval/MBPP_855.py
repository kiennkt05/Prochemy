# MBPP/855
### Completion
def check_Even_Parity(number):
    """
    Check if the given number has even parity.
    
    Parameters:
    number (int): The number to check for even parity.
    
    Returns:
    bool: True if the number has even parity, False otherwise.
    """
    # Convert the number to binary and count the number of 1s
    count_of_ones = bin(number).count('1')
    
    # Check if the count of 1s is even
    return count_of_ones % 2 == 0

# Test case
assert check_Even_Parity(10) == True  # 10 in binary is 1010, which has 2 ones (even)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Even_Parity(10) == True
    assert check_Even_Parity(11) == False
    assert check_Even_Parity(18) == True
