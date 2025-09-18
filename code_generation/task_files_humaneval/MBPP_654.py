# MBPP/654
### Completion
def rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    length (int or float): The length of the rectangle.
    width (int or float): The width of the rectangle.

    Returns:
    int or float: The perimeter of the rectangle.
    """
    return 2 * (length + width)

# Test the function with the provided assertion
assert rectangle_perimeter(10, 20) == 60

# Additional test cases
assert rectangle_perimeter(5, 10) == 30
assert rectangle_perimeter(0, 0) == 0
assert rectangle_perimeter(1.5, 2.5) == 8.0

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rectangle_perimeter(10,20)==60
    assert rectangle_perimeter(10,5)==30
    assert rectangle_perimeter(4,2)==12
