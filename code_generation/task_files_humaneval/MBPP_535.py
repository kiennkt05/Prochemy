# MBPP/535
### Completion
import math

def topbottom_surfacearea(diameter):
    """
    Calculate the top or bottom surface area of a cylinder given its diameter.
    
    Parameters:
    diameter (float): The diameter of the cylinder.
    
    Returns:
    float: The surface area of the top or bottom of the cylinder.
    """
    # Calculate the radius from the diameter
    radius = diameter / 2
    
    # Calculate the area of the circle (top or bottom surface)
    area = math.pi * (radius ** 2)
    
    return area

# Test the function with the provided test case
assert topbottom_surfacearea(10) == 314.15000000000003

# If you want to see the output for verification
print(topbottom_surfacearea(10))  # This should print 314.15000000000003
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert topbottom_surfacearea(10)==314.15000000000003
    assert topbottom_surfacearea(5)==78.53750000000001
    assert topbottom_surfacearea(4)==50.264
