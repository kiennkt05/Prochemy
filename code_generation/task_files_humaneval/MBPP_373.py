# MBPP/373
### Completion
def volume_cuboid(length, width, height):
    """
    Calculate the volume of a cuboid.

    Parameters:
    length (float): The length of the cuboid.
    width (float): The width of the cuboid.
    height (float): The height of the cuboid.

    Returns:
    float: The volume of the cuboid.
    """
    # Calculate the volume using the formula
    volume = length * width * height
    return volume

# Test the function with the provided test case
assert volume_cuboid(1, 2, 3) == 6, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cuboid(1,2,3)==6
    assert volume_cuboid(5,7,9)==315
    assert volume_cuboid(10,15,21)==3150
