# MBPP/814
### Completion
def rombus_area(d1, d2):
    """
    Calculate the area of a rhombus given the lengths of its diagonals.

    Parameters:
    d1 (float): Length of the first diagonal.
    d2 (float): Length of the second diagonal.

    Returns:
    float: Area of the rhombus.
    """
    # Calculate the area using the formula
    area = (d1 * d2) / 2
    return area

# Test the function with the provided test case
assert rombus_area(10, 20) == 100, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rombus_area(10,20)==100
    assert rombus_area(10,5)==25
    assert rombus_area(4,2)==4
