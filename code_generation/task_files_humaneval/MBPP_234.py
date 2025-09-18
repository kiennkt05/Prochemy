# MBPP/234
### Completion
def volume_cube(side: float) -> float:
    """
    Calculate the volume of a cube given the length of its side.

    Parameters:
    side (float): The length of one side of the cube.

    Returns:
    float: The volume of the cube.
    """
    return side ** 3

# Test the function with the provided assertion
assert volume_cube(3) == 27, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125
