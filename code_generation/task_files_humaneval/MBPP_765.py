# MBPP/765
### Completion
def is_polite(n):
    """
    Check if a number is a polite number.
    A polite number is any positive integer that is not a power of 2.
    """
    # A number is a power of 2 if it has only one bit set in its binary representation
    return (n & (n - 1)) != 0

def nth_polite_number(n):
    """
    Find the nth polite number.
    
    Parameters:
    n (int): The position of the polite number to find (1-based index).
    
    Returns:
    int: The nth polite number.
    """
    count = 0  # To count polite numbers found
    current_number = 1  # Start checking from 1
    
    while count < n:
        if is_polite(current_number):
            count += 1  # Increment count if the number is polite
        current_number += 1  # Move to the next number
    
    # The last increment of current_number is unnecessary, so we return current_number - 1
    return current_number - 1

# Test case
assert nth_polite_number(7) == 11  # This should pass as per the provided assertion
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13
