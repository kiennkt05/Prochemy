# MBPP/901
### Completion
import math
from functools import reduce

def lcm(a, b):
    """Calculate the Least Common Multiple of two integers a and b."""
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    """Find the smallest multiple of the first n numbers."""
    return reduce(lcm, range(1, n + 1))

# Test case
assert smallest_multiple(13) == 360360
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_multiple(13)==360360
    assert smallest_multiple(2)==2
    assert smallest_multiple(1)==1
