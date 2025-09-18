# MBPP/354
### Completion
def tn_ap(a, d, n):
    """
    Calculate the n-th term of an arithmetic progression.

    Parameters:
    a (int): The first term of the arithmetic progression.
    d (int): The common difference between the terms.
    n (int): The term number to find.

    Returns:
    int: The n-th term of the arithmetic progression.
    """
    # Calculate the n-th term using the formula
    return a + (n - 1) * d

# Test the function with the provided assertion
assert tn_ap(1, 5, 2) == 9

# Additional test cases
assert tn_ap(1, 5, 1) == 1  # First term
assert tn_ap(1, 5, 3) == 14  # Third term
assert tn_ap(2, 3, 4) == 11  # Fourth term with different values
assert tn_ap(0, 10, 5) == 40  # Fifth term with zero as first term

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tn_ap(1,5,2)==9
    assert tn_ap(2,6,4)==22
    assert tn_ap(1,4,5)==16
