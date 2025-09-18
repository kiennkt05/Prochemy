# MBPP/276
### Completion
import math

def volume_cylinder(radius, height):
    """
    Calculate the volume of a cylinder.

    Parameters:
    radius (float): The radius of the cylinder's base.
    height (float): The height of the cylinder.

    Returns:
    float: The volume of the cylinder.
    """
    # Calculate the volume using the formula: V = π * r^2 * h
    volume = math.pi * (radius ** 2) * height
    return volume

# Test the function with the provided assertion
assert volume_cylinder(10, 5) == 1570.7500000000002

# If the assertion passes, the function works correctly.
print("The function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cylinder(10,5)==1570.7500000000002
    assert volume_cylinder(4,5)==251.32000000000002
    assert volume_cylinder(4,10)==502.64000000000004
