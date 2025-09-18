# MBPP/163
### Completion
import math

def area_polygon(n, s):
    """
    Calculate the area of a regular polygon.

    Parameters:
    n (int): The number of sides of the polygon.
    s (float): The length of each side of the polygon.

    Returns:
    float: The area of the polygon.
    """
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    # Calculate the area using the formula
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

# Test the function with the provided test case
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
