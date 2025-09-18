# MBPP/375
### Completion
def round_num(number, multiple):
    """
    Rounds the given number to the nearest multiple of a specified number.

    Parameters:
    number (int): The number to be rounded.
    multiple (int): The multiple to which the number will be rounded.

    Returns:
    int: The nearest multiple of the specified number.
    """
    if multiple == 0:
        raise ValueError("The multiple cannot be zero.")
    
    # Calculate the remainder of the number when divided by the multiple
    remainder = number % multiple
    
    # Calculate the lower and upper multiples
    lower_multiple = number - remainder
    upper_multiple = lower_multiple + multiple
    
    # Determine which multiple is closer
    if remainder < (multiple / 2):
        return lower_multiple
    else:
        return upper_multiple

# Test case
assert round_num(4722, 10) == 4720

# Additional test cases for verification
assert round_num(4725, 10) == 4730
assert round_num(4724, 10) == 4720
assert round_num(4729, 10) == 4730
assert round_num(4730, 10) == 4730
assert round_num(0, 5) == 0
assert round_num(-3, 5) == -5
assert round_num(-7, 5) == -5

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert round_num(4722,10)==4720
    assert round_num(1111,5)==1110
    assert round_num(219,2)==218
