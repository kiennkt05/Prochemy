# MBPP/85
### Completion
import math

def surfacearea_sphere(radius):
    """
    Calculate the surface area of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The surface area of the sphere.
    """
    # Calculate the surface area using the formula: 4 * π * r^2
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

# Test the function with the provided test case
assert surfacearea_sphere(10) == 1256.6370614359173

# If the assertion passes, the function works correctly for the test case.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_sphere(10)==1256.6370614359173
    assert surfacearea_sphere(15)==2827.4333882308138
    assert surfacearea_sphere(20)==5026.548245743669
