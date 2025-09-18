# MBPP/574
### Completion
import math

def surfacearea_cylinder(radius, height):
    return 2 * math.pi * radius * (height + radius)

# Test the function with the provided assertion
assert surfacearea_cylinder(10, 5) == 942.47798104879  # The expected value is approximately 942.45
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848
