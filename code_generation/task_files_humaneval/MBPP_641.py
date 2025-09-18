# MBPP/641
### Completion
def is_nonagonal(n):
    """
    Calculate the nth nonagonal number using the formula:
    P(n) = n * (7n - 5) / 2
    
    Parameters:
    n (int): The index of the nonagonal number to find.
    
    Returns:
    int: The nth nonagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the nth nonagonal number
    nonagonal_number = n * (7 * n - 5) // 2
    return nonagonal_number

# Test the function with the provided assertion
assert is_nonagonal(10) == 325

# Additional test cases
print(is_nonagonal(1))  # Should return 1
print(is_nonagonal(2))  # Should return 7
print(is_nonagonal(3))  # Should return 19
print(is_nonagonal(4))  # Should return 37
print(is_nonagonal(5))  # Should return 61
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089
