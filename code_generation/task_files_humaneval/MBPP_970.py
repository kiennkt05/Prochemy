# MBPP/970
### Completion
def min_of_two(a, b):
    """
    Returns the minimum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The minimum of the two numbers.
    """
    return a if a < b else b

# Test case
assert min_of_two(10, 20) == 10

# Additional test cases for verification
assert min_of_two(-5, 3) == -5
assert min_of_two(0, 0) == 0
assert min_of_two(7.5, 7.5) == 7.5
assert min_of_two(100, 50) == 50

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_of_two(10,20)==10
    assert min_of_two(19,15)==15
    assert min_of_two(-10,-20)==-20
