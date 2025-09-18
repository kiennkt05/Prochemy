# MBPP/177
### Completion
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def answer(start, end):
    for i in range(start, end + 1):
        for j in range(i + 1, end + 1):  # Ensure j is distinct and greater than i
            current_lcm = lcm(i, j)
            if start <= current_lcm <= end:
                return (i, j)
    return None  # Return None if no such pair is found

# Test the function with the provided assertion
assert answer(3, 8) == (3, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert answer(3,8) == (3,6)
    assert answer(2,6) == (2,4)
    assert answer(1,3) == (1,2)
