# MBPP/188
### Completion
import math

def prod_Square(n):
    """
    Check if the given number can be represented as the product of two squares.
    
    A number can be expressed as a product of two squares if it can be expressed
    as a perfect square.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if the number can be represented as a product of two squares, False otherwise.
    """
    if n < 0:
        return False  # Negative numbers cannot be expressed as a product of two squares.
    
    # Calculate the integer square root of n
    sqrt_n = int(math.isqrt(n))
    
    # Check if the square of the integer square root is equal to n
    return sqrt_n * sqrt_n == n

# Test case
assert prod_Square(25) == False  # 25 is not a product of two squares
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert prod_Square(25) == False
    assert prod_Square(30) == False
    assert prod_Square(16) == True
