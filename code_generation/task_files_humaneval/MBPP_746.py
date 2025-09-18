# MBPP/746
### Completion
import math

def sector_area(radius, angle):
    """
    Calculate the area of a sector of a circle.

    Parameters:
    radius (float): The radius of the circle.
    angle (float): The angle of the sector in degrees.

    Returns:
    float: The area of the sector.
    """
    # Calculate the area using the sector area formula
    area = (angle / 360) * math.pi * (radius ** 2)
    return area

# Test the function with the provided test case
assert sector_area(4, 45) == 6.285714285714286

# If the assertion passes, the function works correctly for this test case.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sector_area(4,45)==6.285714285714286
    assert sector_area(9,45)==31.82142857142857
    assert sector_area(9,360)==None
