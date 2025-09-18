# MBPP/279
### Completion
def decagonal_number(n):
    """
    Calculate the nth decagonal number.

    Parameters:
    n (int): The position in the sequence of decagonal numbers (1-based index).

    Returns:
    int: The nth decagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Using the formula for the nth decagonal number
    return n * (4 * n - 3)

# Test the function with the provided assertion
assert decagonal_number(3) == 27, "Test case failed for n=3"
print("Test case passed for n=3")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370
