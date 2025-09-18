# MBPP/198
### Completion
def largest_triangle(a, b):
    """
    Calculate the area of the largest triangle that can be inscribed in an ellipse
    defined by the semi-major axis 'a' and semi-minor axis 'b'.
    
    Parameters:
    a (float): Semi-major axis of the ellipse.
    b (float): Semi-minor axis of the ellipse.
    
    Returns:
    float: Area of the largest inscribed triangle.
    """
    # Vertices of the triangle
    x1, y1 = a, 0
    x2, y2 = -a, 0
    x3, y3 = 0, b
    
    # Area of the triangle using the determinant formula
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    return area

# Test case
assert largest_triangle(4, 2) == 10.392304845413264
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_triangle(4,2)==10.392304845413264
    assert largest_triangle(5,7)==4.639421805988064
    assert largest_triangle(9,1)==105.2220865598093
