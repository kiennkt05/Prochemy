# MBPP/112
### Completion
import math

def perimeter(radius, height):
    """
    Calculate the perimeter of a cylinder, defined as the sum of the circumference of the base
    and the height of the cylinder.

    Parameters:
    radius (float): The radius of the base of the cylinder.
    height (float): The height of the cylinder.

    Returns:
    float: The perimeter of the cylinder.
    """
    # Calculate the circumference of the base
    circumference = 2 * math.pi * radius
    
    # Calculate the perimeter as the sum of the circumference and height
    perimeter_value = circumference + height
    
    return perimeter_value

# Test the function with the provided assertion
assert perimeter(2, 4) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter(2,4) == 12
    assert perimeter(1,2) == 6
    assert perimeter(3,1) == 8
