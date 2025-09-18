# MBPP/592
### Completion
from math import comb

def sum_of_product(n):
    """
    Calculate the sum of the product of binomial coefficients for a given n.
    
    Parameters:
    n (int): The upper limit for the binomial coefficients.
    
    Returns:
    int: The sum of the product of binomial coefficients.
    """
    total_sum = 0
    for k in range(n + 1):
        binom_coeff = comb(n, k)  # Calculate C(n, k)
        total_sum += binom_coeff * k  # Add the product to the total sum
    return total_sum

# Test case
assert sum_of_product(3) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1
