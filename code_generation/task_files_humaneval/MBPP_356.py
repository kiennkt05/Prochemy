# MBPP/356
### Completion
def find_angle(angle1, angle2):
    """
    Calculate the third angle of a triangle given two angles.

    Parameters:
    angle1 (int): The first angle of the triangle.
    angle2 (int): The second angle of the triangle.

    Returns:
    int: The third angle of the triangle.
    """
    # The sum of angles in a triangle is 180 degrees
    third_angle = 180 - (angle1 + angle2)
    return third_angle

# Test case
assert find_angle(47, 89) == 44, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_angle(47,89)==44
    assert find_angle(45,95)==40
    assert find_angle(50,40)==90
