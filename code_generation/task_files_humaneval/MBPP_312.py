# MBPP/312
### Completion
import math

def volume_cone(radius, height):
    """
    Calculate the volume of a cone.

    Parameters:
    radius (float): The radius of the base of the cone.
    height (float): The height of the cone.

    Returns:
    float: The volume of the cone.
    """
    # Calculate the volume using the formula
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume

# Test the function with the provided test case
assert volume_cone(5, 12) == 314.15926535897927, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cone(5,12)==314.15926535897927
    assert volume_cone(10,15)==1570.7963267948965
    assert volume_cone(19,17)==6426.651371693521
