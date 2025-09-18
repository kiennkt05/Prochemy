# MBPP/850
### Completion
def is_triangle_exists(angle1, angle2, angle3):
    """
    Check if a triangle with positive area can be formed with the given angles.

    Parameters:
    angle1 (int): The first angle in degrees.
    angle2 (int): The second angle in degrees.
    angle3 (int): The third angle in degrees.

    Returns:
    bool: True if a triangle can be formed, False otherwise.
    """
    # Check if all angles are positive
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        return False
    
    # Check if the sum of the angles is 180 degrees
    if angle1 + angle2 + angle3 == 180:
        return True
    else:
        return False

# Test case
assert is_triangle_exists(50, 60, 70) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_triangleexists(50,60,70)==True
    assert is_triangleexists(90,45,45)==True
    assert is_triangleexists(150,30,70)==False
