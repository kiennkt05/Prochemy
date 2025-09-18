# MBPP/252
### Completion
import cmath

def convert(z):
    # Ensure z is a complex number
    if not isinstance(z, complex):
        z = complex(z)
    # Get the polar coordinates
    r, theta = cmath.polar(z)
    return (r, theta)

# Test the function with the provided assertion
assert convert(1) == (1.0, 0.0)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)
