# MBPP/327
### Completion
def check_isosceles(a, b, c):
    """
    Check if a triangle with sides a, b, and c is isosceles.
    
    An isosceles triangle has at least two sides of equal length.
    
    Parameters:
    a (int or float): Length of side a
    b (int or float): Length of side b
    c (int or float): Length of side c
    
    Returns:
    bool: True if the triangle is isosceles, False otherwise
    """
    # Check if at least two sides are equal
    return a == b or a == c or b == c

# Test case
assert check_isosceles(6, 8, 12) == False  # This should return False as no sides are equal
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_isosceles(6,8,12)==False 
    assert check_isosceles(6,6,12)==True
    assert check_isosceles(6,16,20)==False
