# MBPP/519
### Completion
import math

def volume_tetrahedron(a):
    return (a ** 3) / (6 * math.sqrt(2))

# Test the function with the provided assertion
assert round(volume_tetrahedron(10), 2) == 117.85
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_tetrahedron(10)==117.85
    assert volume_tetrahedron(15)==397.75
    assert volume_tetrahedron(20)==942.81
