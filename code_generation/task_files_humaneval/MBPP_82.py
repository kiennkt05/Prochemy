# MBPP/82
### Completion
import math

def volume_sphere(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    # Volume formula for a sphere: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Test case
assert volume_sphere(10) == 4188.790204786391, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_sphere(10)==4188.790204786391
    assert volume_sphere(25)==65449.84694978735
    assert volume_sphere(20)==33510.32163829113
