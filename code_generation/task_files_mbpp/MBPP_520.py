# MBPP/520
### Completion
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def get_lcm(arr):
    return reduce(lcm, arr)

# Test the function with the provided assertion
assert get_lcm([2, 7, 3, 9, 4]) == 252
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_lcm([2, 7, 3, 9, 4]) == 252
    assert get_lcm([1, 2, 8, 3]) == 24
    assert get_lcm([3, 8, 4, 10, 5]) == 120
