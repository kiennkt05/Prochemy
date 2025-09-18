# MBPP/276
### Completion
import math

def volume_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

# Test the function with the provided assertion
assert volume_cylinder(10, 5) == 1570.7500000000002
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cylinder(10,5)==1570.7500000000002
    assert volume_cylinder(4,5)==251.32000000000002
    assert volume_cylinder(4,10)==502.64000000000004
