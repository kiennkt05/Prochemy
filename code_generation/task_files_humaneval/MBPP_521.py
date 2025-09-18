# MBPP/521
### Completion
def check_scalene(a, b, c):
    """
    Check if a triangle with sides a, b, and c is scalene.
    
    A scalene triangle has all sides of different lengths.
    
    Parameters:
    a (int or float): Length of the first side.
    b (int or float): Length of the second side.
    c (int or float): Length of the third side.
    
    Returns:
    bool: True if the triangle is scalene, False otherwise.
    """
    return a != b and b != c and a != c

# Test case
assert check_scalene(6, 8, 12) == True  # This should return True as all sides are different
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_isosceles(6,8,12)==True
    assert check_isosceles(6,6,12)==False
    assert check_isosceles(6,15,20)==True
