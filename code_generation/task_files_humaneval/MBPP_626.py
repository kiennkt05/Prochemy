# MBPP/626
### Completion
def triangle_area(r):
    """
    Calculate the area of the largest triangle that can be inscribed in a semicircle of radius r.
    
    Parameters:
    r (float): The radius of the semicircle.
    
    Returns:
    float: The area of the largest inscribed triangle.
    """
    # The area of the largest triangle inscribed in a semicircle is r^2
    return r ** 2

# Test cases
assert triangle_area(0) == 0  # Area should be 0 when radius is 0
assert triangle_area(1) == 1  # Area should be 1 when radius is 1
assert triangle_area(2) == 4  # Area should be 4 when radius is 2
assert triangle_area(3) == 9  # Area should be 9 when radius is 3

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert triangle_area(0) == 0
    assert triangle_area(-1) == -1
    assert triangle_area(2) == 4
