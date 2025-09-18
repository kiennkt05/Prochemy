# MBPP/887
### Completion
def is_odd(number):
    """
    Check if the given number is odd using a bitwise operator.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is odd, False otherwise.
    """
    return (number & 1) == 1

# Test case
assert is_odd(5) == True  # 5 is odd
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_odd(5) == True
    assert is_odd(6) == False
    assert is_odd(7) == True
