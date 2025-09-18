# MBPP/499
### Completion
def diameter_circle(radius):
    """
    Calculate the diameter of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The diameter of the circle.
    """
    # The diameter is twice the radius
    return 2 * radius

# Test case
assert diameter_circle(10) == 20, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert diameter_circle(10)==20
    assert diameter_circle(40)==80
    assert diameter_circle(15)==30
