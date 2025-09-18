# MBPP/233
### Completion
import math

def lateral_surface_cylinder(radius, height):
    """
    Calculate the lateral surface area of a cylinder.

    Parameters:
    radius (float): The radius of the cylinder.
    height (float): The height of the cylinder.

    Returns:
    float: The lateral surface area of the cylinder.
    """
    # Calculate the lateral surface area using the formula
    lateral_surface_area = 2 * math.pi * radius * height
    return lateral_surface_area

# Test the function with the provided assertion
assert lateral_surface_cylinder(10, 5) == 314.15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsuface_cylinder(10,5)==314.15000000000003
    assert lateralsuface_cylinder(4,5)==125.66000000000001
    assert lateralsuface_cylinder(4,10)==251.32000000000002
