# MBPP/901
### Completion
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def smallest_multiple(n):
    return reduce(lcm, range(1, n + 1))

# Test the function with the provided assertion
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
