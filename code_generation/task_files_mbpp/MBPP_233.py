# MBPP/233
### Completion
import math

def lateralsurface_cylinder(radius, height):
    return 2 * math.pi * radius * height

# Test the function with the provided assertion
assert lateralsurface_cylinder(10, 5) == 314.15000000000003
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsuface_cylinder(10,5)==314.15000000000003
    assert lateralsuface_cylinder(4,5)==125.66000000000001
    assert lateralsuface_cylinder(4,10)==251.32000000000002
