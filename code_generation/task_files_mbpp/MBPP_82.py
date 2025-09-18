# MBPP/82
### Completion
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Test the function with the provided assertion
assert volume_sphere(10) == 4188.790204786391
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_sphere(10)==4188.790204786391
    assert volume_sphere(25)==65449.84694978735
    assert volume_sphere(20)==33510.32163829113
