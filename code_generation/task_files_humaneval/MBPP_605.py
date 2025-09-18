# MBPP/605
### Completion
import math

def prime_num(n):
    """
    Check if the given integer n is a prime number.

    Parameters:
    n (int): The integer to check.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    # Check for numbers less than 2
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test case
assert prime_num(13) == True  # 13 is a prime number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False
