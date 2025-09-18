# MBPP/518
### Completion
import math

def sqrt_root(n):
    # Check if the number is a perfect square
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    root = math.isqrt(n)  # Use integer square root to avoid floating point issues
    if root * root == n:
        return root
    else:
        raise ValueError(f"{n} is not a perfect square.")

# Test the function with the provided assertion
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
