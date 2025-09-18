# MBPP/497
### Completion
import math

def surfacearea_cone(radius, slant_height):
    """
    Calculate the surface area of a cone.

    Parameters:
    radius (float): The radius of the base of the cone.
    slant_height (float): The slant height of the cone.

    Returns:
    float: The surface area of the cone.
    """
    # Calculate the surface area using the formula
    surface_area = math.pi * radius * (radius + slant_height)
    return surface_area

# Test the function with the provided test case
assert surfacearea_cone(5, 12) == 282.7433388230814
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cone(5,12)==282.7433388230814
    assert surfacearea_cone(10,15)==880.5179353159282
    assert surfacearea_cone(19,17)==2655.923961165254
