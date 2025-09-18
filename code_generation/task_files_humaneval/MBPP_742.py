# MBPP/742
### Completion
import math

def area_tetrahedron(a):
    """
    Calculate the surface area of a regular tetrahedron given the edge length.

    Parameters:
    a (float): The length of an edge of the tetrahedron.

    Returns:
    float: The surface area of the tetrahedron.
    """
    # Calculate the surface area using the formula for a regular tetrahedron
    area = math.sqrt(3) * (a ** 2)
    return area

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894, "Test case failed!"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772
