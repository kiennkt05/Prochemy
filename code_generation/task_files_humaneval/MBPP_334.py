# MBPP/334
### Completion
def check_Validity(a, b, c):
    """
    Check if a triangle with sides a, b, and c is valid.

    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c

    Returns:
    bool: True if the triangle is valid, False otherwise
    """
    # Check the triangle inequality conditions
    return (a + b > c) and (a + c > b) and (b + c > a)

# Test cases
assert check_Validity(1, 2, 3) == False  # This should return False
assert check_Validity(3, 4, 5) == True   # This should return True
assert check_Validity(5, 1, 1) == False  # This should return False
assert check_Validity(7, 10, 5) == True   # This should return True
assert check_Validity(0, 1, 1) == False   # This should return False (sides cannot be zero or negative)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Validity(1,2,3) == False
    assert check_Validity(2,3,5) == False
    assert check_Validity(7,10,5) == True
