# MBPP/738
### Completion
def geometric_sum(n):
    """
    Calculate the geometric sum of n-1 terms where the first term is 1
    and the common ratio is 1/2.

    Parameters:
    n (int): The number of terms in the series (n-1 terms will be summed).

    Returns:
    float: The geometric sum of the series.
    """
    if n <= 1:
        return 0.0  # If n is 1 or less, the sum is 0 since there are no terms to sum.
    
    # Calculate the geometric sum
    r = 0.5  # common ratio
    sum_value = 2 * (1 - (r ** (n - 1)))  # Geometric sum formula
    return sum_value

# Test case
assert geometric_sum(7) == 1.9921875, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375
