# MBPP/441
### Completion
def surfacearea_cube(side):
    """
    Calculate the surface area of a cube.

    Parameters:
    side (float or int): The length of one edge of the cube.

    Returns:
    float: The surface area of the cube.
    """
    # Calculate the surface area using the formula
    surface_area = 6 * (side ** 2)
    return surface_area

# Test the function with the provided test case
assert surfacearea_cube(5) == 150, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600
