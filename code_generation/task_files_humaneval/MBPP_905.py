# MBPP/905
### Completion
import math

def sum_of_square(n):
    """
    Calculate the sum of squares of binomial coefficients for a given n.
    
    Parameters:
    n (int): The upper limit for the binomial coefficients.
    
    Returns:
    int: The sum of squares of binomial coefficients C(n, k) for k = 0 to n.
    """
    total_sum = 0
    for k in range(n + 1):
        # Calculate the binomial coefficient C(n, k)
        binomial_coefficient = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        # Add the square of the binomial coefficient to the total sum
        total_sum += binomial_coefficient ** 2
    return total_sum

# Test case
assert sum_of_square(4) == 70
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_square(4) == 70
    assert sum_of_square(5) == 252
    assert sum_of_square(2) == 6
