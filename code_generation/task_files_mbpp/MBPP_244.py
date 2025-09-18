# MBPP/244
### Completion
import math

def next_Perfect_Square(n):
    # Calculate the square root of the given number
    root = math.isqrt(n)
    # Find the next integer greater than the square root
    next_root = root + 1
    # Return the next perfect square
    return next_root * next_root

# Test the function with the provided assertion
assert next_Perfect_Square(35) == 36
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16
