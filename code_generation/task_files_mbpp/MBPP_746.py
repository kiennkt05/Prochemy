# MBPP/746
### Completion
import math

def sector_area(radius, angle):
    return (angle / 360) * math.pi * (radius ** 2)

# Test the function with the provided assertion
assert sector_area(4, 45) == 6.285714285714286
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sector_area(4,45)==6.285714285714286
    assert sector_area(9,45)==31.82142857142857
    assert sector_area(9,360)==None
