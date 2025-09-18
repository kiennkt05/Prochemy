# MBPP/287
### Completion
def square_Sum(n):
    """
    Calculate the sum of squares of the first n even natural numbers.

    Parameters:
    n (int): The number of even natural numbers to consider.

    Returns:
    int: The sum of squares of the first n even natural numbers.
    """
    # Calculate the sum of squares of the first n even natural numbers
    return sum((2 * i) ** 2 for i in range(1, n + 1))

# Test case
assert square_Sum(2) == 20  # 2^2 + 4^2 = 4 + 16 = 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_Sum(2) == 20
    assert square_Sum(3) == 56
    assert square_Sum(4) == 120
