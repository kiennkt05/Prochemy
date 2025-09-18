# MBPP/379
### Completion
def surfacearea_cuboid(length, width, height):
    """
    Calculate the surface area of a cuboid.

    Parameters:
    length (float): The length of the cuboid.
    width (float): The width of the cuboid.
    height (float): The height of the cuboid.

    Returns:
    float: The surface area of the cuboid.
    """
    # Calculate the surface area using the formula
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

# Test the function with the provided test case
assert surfacearea_cuboid(1, 2, 3) == 22

# You can add more test cases if needed
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cuboid(1,2,3)==22
    assert surfacearea_cuboid(5,7,9)==286
    assert surfacearea_cuboid(10,15,21)==1350
