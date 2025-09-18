# MBPP/677
### Completion
def validity_triangle(angle1, angle2, angle3):
    """
    Check if the given angles can form a valid triangle.

    Parameters:
    angle1 (int): The first angle of the triangle.
    angle2 (int): The second angle of the triangle.
    angle3 (int): The third angle of the triangle.

    Returns:
    bool: True if the angles form a valid triangle, False otherwise.
    """
    # Check if all angles are greater than 0 and their sum is 180
    return angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180

# Test case
assert validity_triangle(60, 50, 90) == False  # This should return False since 60 + 50 + 90 = 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert validity_triangle(60,50,90)==False
    assert validity_triangle(45,75,60)==True
    assert validity_triangle(30,50,100)==True
