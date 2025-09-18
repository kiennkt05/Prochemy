# MBPP/830
### Completion
import math

def round_up(number, digits):
    """
    Rounds up a number to a specified number of decimal places.

    Parameters:
    number (float): The number to be rounded up.
    digits (int): The number of decimal places to round up to.

    Returns:
    float: The rounded up number.
    """
    if digits < 0:
        # If digits is negative, round up to the nearest integer
        return math.ceil(number)
    else:
        # Scale the number, apply ceil, and scale back
        factor = 10 ** digits
        return math.ceil(number * factor) / factor

# Test case
assert round_up(123.01247, 0) == 124
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert round_up(123.01247,0)==124
    assert round_up(123.01247,1)==123.1
    assert round_up(123.01247,2)==123.02
