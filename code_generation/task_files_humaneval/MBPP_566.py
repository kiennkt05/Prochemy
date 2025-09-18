# MBPP/566
### Completion
def sum_digits(n: int) -> int:
    """
    Calculate the sum of the digits of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose digits will be summed.

    Returns:
    int: The sum of the digits of the integer.
    
    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Convert the integer to a string, iterate over each character,
    # convert it back to an integer, and sum them up.
    return sum(int(digit) for digit in str(n))

# Test case
assert sum_digits(345) == 12  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16
