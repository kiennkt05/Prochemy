# MBPP/86
### Completion
def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    Parameters:
    n (int): The index of the centered hexagonal number to calculate.

    Returns:
    int: The nth centered hexagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Using the formula for the nth centered hexagonal number
    return 3 * n * (n - 1) + 1

# Test case
assert centered_hexagonal_number(10) == 271, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217
