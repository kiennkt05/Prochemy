# MBPP/404
### Completion
def minimum(a, b):
    """
    Returns the minimum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The minimum of the two numbers.
    """
    if a < b:
        return a
    else:
        return b

# Test case
assert minimum(1, 2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert minimum(1,2) == 1
    assert minimum(-5,-4) == -5
    assert minimum(0,0) == 0
