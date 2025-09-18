# MBPP/244
### Completion
import math

def next_Perfect_Square(n):
    """
    Find the next perfect square greater than the given number n.

    Parameters:
    n (int): The number to find the next perfect square greater than.

    Returns:
    int: The next perfect square greater than n.
    """
    # Calculate the integer square root of n
    root = math.isqrt(n)
    
    # Increment the root to find the next integer
    next_root = root + 1
    
    # Return the next perfect square
    return next_root ** 2

# Test case
assert next_Perfect_Square(35) == 36

# Additional test cases
assert next_Perfect_Square(0) == 1
assert next_Perfect_Square(1) == 4
assert next_Perfect_Square(15) == 16
assert next_Perfect_Square(24) == 25
assert next_Perfect_Square(49) == 64

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16
