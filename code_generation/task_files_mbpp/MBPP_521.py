# MBPP/521
### Completion
def check_scalene(a, b, c):
    """
    Check if a triangle with sides a, b, and c is scalene.
    
    A scalene triangle has all sides of different lengths.
    
    Parameters:
    a (int or float): Length of side a
    b (int or float): Length of side b
    c (int or float): Length of side c
    
    Returns:
    bool: True if the triangle is scalene, False otherwise
    """
    return a != b and b != c and a != c

# Test the function with an assertion
assert check_scalene(6, 8, 12) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_isosceles(6,8,12)==True
    assert check_isosceles(6,6,12)==False
    assert check_isosceles(6,15,20)==True
