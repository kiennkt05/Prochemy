# MBPP/606
### Completion
import math

def radian_degree(degrees):
    """
    Convert degrees to radians.

    Parameters:
    degrees (float): The angle in degrees to be converted.

    Returns:
    float: The angle in radians.
    """
    # Convert degrees to radians
    radians = degrees * (math.pi / 180)
    return radians

# Test case
assert radian_degree(90) == 1.5707963267948966

# You can add more test cases if needed
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert radian_degree(90)==1.5707963267948966
    assert radian_degree(60)==1.0471975511965976
    assert radian_degree(120)==2.0943951023931953
