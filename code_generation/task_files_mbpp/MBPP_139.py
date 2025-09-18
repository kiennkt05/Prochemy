# MBPP/139
### Completion
import math

def circle_circumference(radius):
    return 2 * math.pi * radius

# Test the function with the provided assertion
assert circle_circumference(10) == 62.830000000000005
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert circle_circumference(10)==62.830000000000005
    assert circle_circumference(5)==31.415000000000003
    assert circle_circumference(4)==25.132
