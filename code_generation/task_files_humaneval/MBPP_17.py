# MBPP/17
### Completion
def square_perimeter(side_length):
    """
    Calculate the perimeter of a square.

    Parameters:
    side_length (int or float): The length of one side of the square.

    Returns:
    int or float: The perimeter of the square.
    """
    return 4 * side_length

# Test case
assert square_perimeter(10) == 40, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16
