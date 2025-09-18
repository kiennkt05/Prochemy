# MBPP/151
### Completion
import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

# Test the function with the provided assertion
assert is_coprime(17, 13) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_coprime(17,13) == True
    assert is_coprime(15,21) == False
    assert is_coprime(25,45) == False
