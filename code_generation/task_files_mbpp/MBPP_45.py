# MBPP/45
### Completion
from math import gcd
from functools import reduce

def get_gcd(arr):
    return reduce(gcd, arr)

# Test the function with the provided assertion
assert get_gcd([2, 4, 6, 8, 16]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_gcd([2, 4, 6, 8, 16]) == 2
    assert get_gcd([1, 2, 3]) == 1
    assert get_gcd([2, 4, 6, 8]) == 2 
