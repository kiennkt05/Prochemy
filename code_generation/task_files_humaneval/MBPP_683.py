# MBPP/683
### Completion
import math

def sum_Square(n):
    """
    Check if the given number can be represented as the sum of two squares.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number can be expressed as the sum of two squares, False otherwise.
    """
    if n < 0:
        return False  # Negative numbers cannot be expressed as the sum of two squares
    if n == 0:
        return True   # 0 can be expressed as 0^2 + 0^2

    # Check for each integer a from 0 to sqrt(n)
    for a in range(int(math.isqrt(n)) + 1):
        b_squared = n - a * a
        if b_squared < 0:
            continue
        b = int(math.isqrt(b_squared))
        if b * b == b_squared:
            return True
            
    return False

# Test case
assert sum_Square(25) == True  # 25 = 3^2 + 4^2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Square(25) == True
    assert sum_Square(24) == False
    assert sum_Square(17) == True
