# MBPP/518
### Completion
import math

def sqrt_root(n):
    """
    Calculate the square root of a perfect number.

    Parameters:
    n (int): A perfect number (should be a perfect square).

    Returns:
    int: The square root of the perfect number if it is a perfect square.
    
    Raises:
    ValueError: If n is not a perfect square.
    """
    # Calculate the integer square root of n
    root = int(math.isqrt(n))
    
    # Check if n is a perfect square
    if root * root == n:
        return root
    else:
        raise ValueError(f"{n} is not a perfect square.")

# Test case
assert sqrt_root(4) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sqrt_root(4)==2
    assert sqrt_root(16)==4
    assert sqrt_root(400)==20
