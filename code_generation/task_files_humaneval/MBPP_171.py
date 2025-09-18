# MBPP/171
### Completion
def perimeter_pentagon(side_length):
    """
    Calculate the perimeter of a regular pentagon.

    Parameters:
    side_length (float or int): The length of one side of the pentagon.

    Returns:
    float or int: The perimeter of the pentagon.
    """
    # A pentagon has 5 equal sides
    perimeter = side_length * 5
    return perimeter

# Test case
assert perimeter_pentagon(5) == 25, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_pentagon(5)==25
    assert perimeter_pentagon(10)==50
    assert perimeter_pentagon(15)==75
