# MBPP/924
### Completion
def max_of_two(a, b):
    """
    Returns the maximum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The maximum of the two numbers.
    """
    if a > b:
        return a
    else:
        return b

# Test case
assert max_of_two(10, 20) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_of_two(10,20)==20
    assert max_of_two(19,15)==19
    assert max_of_two(-10,-20)==-10
