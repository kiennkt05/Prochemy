# MBPP/369
### Completion
def lateral_surface_cuboid(length, width, height):
    """
    Calculate the lateral surface area of a cuboid.

    Parameters:
    length (float): The length of the cuboid.
    width (float): The width of the cuboid.
    height (float): The height of the cuboid.

    Returns:
    float: The lateral surface area of the cuboid.
    """
    # Calculate the lateral surface area using the formula
    lateral_surface_area = 2 * height * (length + width)
    return lateral_surface_area

# Test the function with the provided test case
assert lateral_surface_cuboid(8, 5, 6) == 156, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cuboid(8,5,6)==156
    assert lateralsurface_cuboid(7,9,10)==320
    assert lateralsurface_cuboid(10,20,30)==1800
