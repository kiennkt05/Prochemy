# MBPP/606
### Completion
import math

def radian_degree(degrees):
    """Convert degrees to radians."""
    return degrees * (math.pi / 180)

# Test the function with the provided assertion
assert radian_degree(90) == 1.5707963267948966
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert radian_degree(90)==1.5707963267948966
    assert radian_degree(60)==1.0471975511965976
    assert radian_degree(120)==2.0943951023931953
