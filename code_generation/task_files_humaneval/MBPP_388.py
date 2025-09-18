# MBPP/388
### Completion
def highest_Power_of_2(n):
    """
    Function to find the highest power of 2 that is less than or equal to n.
    
    Parameters:
    n (int): The number to find the highest power of 2 for.
    
    Returns:
    int: The highest power of 2 less than or equal to n.
    """
    if n < 1:
        return 0  # If n is less than 1, there is no power of 2 that is less than or equal to n.
    
    power = 1  # Start with 2^0
    while power <= n:
        power *= 2  # Move to the next power of 2
    
    return power // 2  # Return the last valid power of 2

# Test case
assert highest_Power_of_2(10) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32
