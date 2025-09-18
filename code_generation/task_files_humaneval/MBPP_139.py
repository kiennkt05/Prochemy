# MBPP/139
### Completion
import math

def circle_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The circumference of the circle.
    """
    # Calculate the circumference using the formula
    circumference = 2 * math.pi * radius
    return circumference

# Test the function with the provided test case
assert circle_circumference(10) == 62.830000000000005
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert circle_circumference(10)==62.830000000000005
    assert circle_circumference(5)==31.415000000000003
    assert circle_circumference(4)==25.132
