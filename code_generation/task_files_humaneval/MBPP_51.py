# MBPP/51
### Completion
def check_equilateral(side1, side2, side3):
    """
    Check if a triangle is equilateral.

    Parameters:
    side1 (int or float): Length of the first side of the triangle.
    side2 (int or float): Length of the second side of the triangle.
    side3 (int or float): Length of the third side of the triangle.

    Returns:
    bool: True if the triangle is equilateral, False otherwise.
    """
    # An equilateral triangle has all three sides equal
    return side1 == side2 == side3

# Test case
assert check_equilateral(6, 8, 12) == False  # This should return False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_equilateral(6,8,12)==False 
    assert check_equilateral(6,6,12)==False
    assert check_equilateral(6,6,6)==True
