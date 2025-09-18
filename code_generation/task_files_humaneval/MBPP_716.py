# MBPP/716
### Completion
def rombus_perimeter(side_length):
    """
    Calculate the perimeter of a rhombus.

    Parameters:
    side_length (float): The length of one side of the rhombus.

    Returns:
    float: The perimeter of the rhombus.
    """
    return 4 * side_length

# Test case
assert rombus_perimeter(10) == 40, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rombus_perimeter(10)==40
    assert rombus_perimeter(5)==20
    assert rombus_perimeter(4)==16
