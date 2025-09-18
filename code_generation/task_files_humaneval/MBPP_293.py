# MBPP/293
### Completion
import math

def otherside_rightangle(side1, side2):
    """
    Calculate the length of the third side of a right-angled triangle
    given the lengths of the other two sides.

    Parameters:
    side1 (float): Length of the first side.
    side2 (float): Length of the second side.

    Returns:
    float: Length of the hypotenuse calculated using the Pythagorean theorem.
    """
    # Calculate the hypotenuse using the Pythagorean theorem
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

# Test case
assert abs(otherside_rightangle(7, 8) - 10.63014581273465) < 1e-9, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert otherside_rightangle(7,8)==10.63014581273465
    assert otherside_rightangle(3,4)==5
    assert otherside_rightangle(7,15)==16.55294535724685
