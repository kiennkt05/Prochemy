# MBPP/761
### Completion
import math

def arc_length(radius, angle_degrees):
    """
    Calculate the arc length of a circle given the radius and angle in degrees.

    Parameters:
    radius (float): The radius of the circle.
    angle_degrees (float): The angle in degrees.

    Returns:
    float: The arc length corresponding to the given radius and angle.
    """
    # Convert angle from degrees to radians
    angle_radians = angle_degrees * (math.pi / 180)
    
    # Calculate arc length
    length = radius * angle_radians
    
    return length

# Test case
assert arc_length(9, 45) == 3.5357142857142856
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert arc_length(9,45)==3.5357142857142856
    assert arc_length(9,480)==None
    assert arc_length(5,270)==11.785714285714285
