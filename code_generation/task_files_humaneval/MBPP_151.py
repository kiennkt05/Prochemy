# MBPP/151
### Completion
import math

def is_coprime(a, b):
    """
    Check if two numbers are co-prime.
    
    Two numbers are co-prime if their greatest common divisor (GCD) is 1.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    bool: True if a and b are co-prime, False otherwise.
    """
    return math.gcd(a, b) == 1

# Test case
assert is_coprime(17, 13) == True  # 17 and 13 are co-prime
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_coprime(17,13) == True
    assert is_coprime(15,21) == False
    assert is_coprime(25,45) == False
