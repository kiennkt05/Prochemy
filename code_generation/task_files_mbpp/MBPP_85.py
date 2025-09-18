# MBPP/85
### Completion
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

# Test the function with the provided assertion
assert surfacearea_sphere(10) == 1256.6370614359173
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_sphere(10)==1256.6370614359173
    assert surfacearea_sphere(15)==2827.4333882308138
    assert surfacearea_sphere(20)==5026.548245743669
