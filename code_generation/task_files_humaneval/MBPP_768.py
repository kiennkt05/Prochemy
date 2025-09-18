# MBPP/768
### Completion
def check_Odd_Parity(number):
    """
    Check if the given number has odd parity.
    
    Parameters:
    number (int): The number to check for odd parity.
    
    Returns:
    bool: True if the number has odd parity, False otherwise.
    """
    # Convert the number to binary and count the number of '1's
    count_of_ones = bin(number).count('1')
    
    # Check if the count of 1s is odd
    return count_of_ones % 2 == 1

# Test case
assert check_Odd_Parity(13) == True  # 13 in binary is 1101, which has 3 ones (odd)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Odd_Parity(13) == True
    assert check_Odd_Parity(21) == True
    assert check_Odd_Parity(18) == False
