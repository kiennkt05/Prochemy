# MBPP/731
### Completion
import math

def lateralsurface_cone(radius, slant_height):
    """
    Calculate the lateral surface area of a cone.

    Parameters:
    radius (float): The radius of the base of the cone.
    slant_height (float): The slant height of the cone.

    Returns:
    float: The lateral surface area of the cone.
    """
    # Calculate the lateral surface area using the formula
    lateral_surface_area = math.pi * radius * slant_height
    return lateral_surface_area

# Test the function with the provided test case
assert lateralsurface_cone(5, 12) == 204.20352248333654

# If you want to see the output for the test case, you can uncomment the following line:
# print(lateralsurface_cone(5, 12))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388
