# MBPP/135
### Completion
def hexagonal_num(n):
    """
    Calculate the nth hexagonal number.

    Parameters:
    n (int): The position in the sequence of hexagonal numbers.

    Returns:
    int: The nth hexagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the nth hexagonal number using the formula
    return n * (2 * n - 1)

# Test case
assert hexagonal_num(10) == 190, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91
