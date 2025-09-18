# MBPP/520
### Completion
import math
from functools import reduce

def lcm(a, b):
    """Calculate the least common multiple of two integers a and b."""
    return abs(a * b) // math.gcd(a, b)

def get_lcm(arr):
    """Calculate the least common multiple of an array of integers."""
    return reduce(lcm, arr)

# Test case
assert get_lcm([2, 7, 3, 9, 4]) == 252

# Additional test cases
assert get_lcm([1, 2, 3]) == 6
assert get_lcm([5, 10, 15]) == 30
assert get_lcm([12, 15, 20]) == 60
assert get_lcm([7, 14, 21]) == 42

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_lcm([2, 7, 3, 9, 4]) == 252
    assert get_lcm([1, 2, 8, 3]) == 24
    assert get_lcm([3, 8, 4, 10, 5]) == 120
