# MBPP/848
### Completion
def area_trapezium(a, b, h):
    """
    Calculate the area of a trapezium.

    Parameters:
    a (float): Length of the first parallel side.
    b (float): Length of the second parallel side.
    h (float): Height of the trapezium.

    Returns:
    float: Area of the trapezium.
    """
    # Calculate the area using the trapezium area formula
    area = 0.5 * (a + b) * h
    return area

# Test the function with the provided test case
assert area_trapezium(6, 9, 4) == 30, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert area_trapezium(6,9,4)==30
    assert area_trapezium(10,20,30)==450
    assert area_trapezium(15,25,35)==700
