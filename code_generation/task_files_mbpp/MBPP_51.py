# MBPP/51
### Completion
def check_equilateral(a, b, c):
    """
    Check if a triangle with sides a, b, and c is equilateral.

    Parameters:
    a (int or float): Length of side a
    b (int or float): Length of side b
    c (int or float): Length of side c

    Returns:
    bool: True if the triangle is equilateral, False otherwise
    """
    return a == b == c

# Example assertion
assert check_equilateral(6, 8, 12) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_equilateral(6,8,12)==False 
    assert check_equilateral(6,6,12)==False
    assert check_equilateral(6,6,6)==True
