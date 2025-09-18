# MBPP/789
### Completion
def perimeter_polygon(num_sides, side_length):
    """
    Calculate the perimeter of a regular polygon.

    Parameters:
    num_sides (int): The number of sides of the polygon.
    side_length (float): The length of each side of the polygon.

    Returns:
    float: The perimeter of the polygon.
    """
    # Calculate the perimeter using the formula
    perimeter = num_sides * side_length
    return perimeter

# Test case
assert perimeter_polygon(4, 20) == 80, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_polygon(4,20)==80
    assert perimeter_polygon(10,15)==150
    assert perimeter_polygon(9,7)==63
