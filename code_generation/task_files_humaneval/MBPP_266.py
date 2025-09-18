# MBPP/266
### Completion
def lateralsurface_cube(side):
    """
    Calculate the lateral surface area of a cube.

    Parameters:
    side (float): The length of one edge of the cube.

    Returns:
    float: The lateral surface area of the cube.
    """
    # Calculate the lateral surface area using the formula
    lateral_surface_area = 4 * (side ** 2)
    return lateral_surface_area

# Test the function with the provided test case
assert lateralsurface_cube(5) == 100, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400
