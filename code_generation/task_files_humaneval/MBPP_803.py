# MBPP/803
### Completion
import math

def is_Perfect_Square(n):
    """
    Check if the given number n is a perfect square.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False  # Negative numbers cannot be perfect squares
    root = int(math.isqrt(n))  # Get the integer square root of n
    return root * root == n  # Check if squaring the root gives n

# Test case
assert is_Perfect_Square(10) == False  # 10 is not a perfect square
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Perfect_Square(10) == False
    assert is_Perfect_Square(36) == True
    assert is_Perfect_Square(14) == False
