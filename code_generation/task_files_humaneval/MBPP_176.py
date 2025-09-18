# MBPP/176
### Completion
def perimeter_triangle(a, b, c):
    """
    Calculate the perimeter of a triangle given the lengths of its three sides.

    Parameters:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    float: The perimeter of the triangle.
    """
    return a + b + c

# Test case
assert perimeter_triangle(10, 20, 30) == 60, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_triangle(10,20,30)==60
    assert perimeter_triangle(3,4,5)==12
    assert perimeter_triangle(25,35,45)==105
