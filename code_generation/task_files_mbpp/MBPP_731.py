# MBPP/731
### Completion
import math

def lateralsurface_cone(radius, slant_height):
    return math.pi * radius * slant_height

# Test the function with the provided assertion
assert lateralsurface_cone(5, 12) == 204.20352248333654
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388
