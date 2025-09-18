# MBPP/830
### Completion
import math

def round_up(number, digits):
    """
    Rounds up a number to a specified number of decimal places.

    Parameters:
    number (float): The number to round up.
    digits (int): The number of decimal places to round up to.

    Returns:
    float: The rounded up number.
    """
    factor = 10 ** digits
    return math.ceil(number * factor) / factor

# Example usage
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
