# MBPP/3
### Completion
import math

def is_not_prime(n):
    """
    Determine if a number is non-prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is non-prime, False if it is prime.
    """
    if n < 2:
        return True  # 0, 1, and negative numbers are non-prime
    if n == 2:
        return False  # 2 is a prime number
    if n % 2 == 0:
        return True  # Any even number greater than 2 is non-prime
    
    # Check for factors from 3 to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return True  # Found a factor, so n is non-prime
    
    return False  # No factors found, n is prime

# Test case
assert is_not_prime(2) == False  # 2 is prime
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_not_prime(2) == False
    assert is_not_prime(10) == True
    assert is_not_prime(35) == True
