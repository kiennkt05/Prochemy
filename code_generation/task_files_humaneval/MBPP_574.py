# MBPP/574
### Completion
import math

def surfacearea_cylinder(height, radius):
    """
    Calculate the surface area of a cylinder.

    Parameters:
    height (float): The height of the cylinder.
    radius (float): The radius of the cylinder's base.

    Returns:
    float: The surface area of the cylinder rounded to two decimal places.
    """
    # Calculate the surface area using the formula
    surface_area = 2 * math.pi * radius * (height + radius)
    
    # Return the surface area rounded to two decimal places
    return round(surface_area, 2)

# Test the function with the provided assertion
assert surfacearea_cylinder(10, 5) == 942.45
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848
