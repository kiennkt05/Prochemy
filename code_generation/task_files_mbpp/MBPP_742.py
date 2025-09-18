# MBPP/742
### Completion
import math

def area_tetrahedron(a):
    return math.sqrt(3) * a**2

# Test the function with the provided assertion
assert area_tetrahedron(3) == 15.588457268119894
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772
