# MBPP/309
### Completion
def maximum(a, b):
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
assert maximum(5, 10) == 10  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximum(5,10) == 10
    assert maximum(-1,-2) == -1
    assert maximum(9,7) == 9
