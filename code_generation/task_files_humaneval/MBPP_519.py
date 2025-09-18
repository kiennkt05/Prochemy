# MBPP/519
### Completion
import math

def volume_tetrahedron(a):
    """
    Calculate the volume of a regular tetrahedron given the length of its edge.
    
    Parameters:
    a (float): The length of the edge of the tetrahedron.
    
    Returns:
    float: The volume of the tetrahedron.
    """
    # Volume formula for a regular tetrahedron
    volume = (a ** 3) / (6 * math.sqrt(2))
    return volume

# Test the function with the provided assertion
assert abs(volume_tetrahedron(10) - 117.85) < 0.01, "Test case failed!"
print("Test case passed! Volume of tetrahedron with edge length 10 is approximately 117.85.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_tetrahedron(10)==117.85
    assert volume_tetrahedron(15)==397.75
    assert volume_tetrahedron(20)==942.81
