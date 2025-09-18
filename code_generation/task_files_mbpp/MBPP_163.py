# MBPP/163
### Completion
import math

def area_polygon(n, s):
    """
    Calculate the area of a regular polygon.

    Parameters:
    n (int): Number of sides of the polygon
    s (float): Length of each side

    Returns:
    float: Area of the polygon
    """
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

# Test the function with the provided assertion
assert area_polygon(4, 20) == 400.00000000000006
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_polygon(4,20)==400.00000000000006
    assert area_polygon(10,15)==1731.1969896610804
    assert area_polygon(9,7)==302.90938549487214
