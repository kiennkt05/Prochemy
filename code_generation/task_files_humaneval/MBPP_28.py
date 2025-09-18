# MBPP/28
### Completion
import math

def binomial_Coeff(n, k):
    """
    Calculate the binomial coefficient C(n, k).
    
    Parameters:
    n (int): Total number of items.
    k (int): Number of items to choose.
    
    Returns:
    int: The binomial coefficient C(n, k).
    """
    if k < 0 or k > n:
        return 0  # C(n, k) is defined as 0 if k < 0 or k > n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Test case
assert binomial_Coeff(5, 2) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binomial_Coeff(5,2) == 10
    assert binomial_Coeff(4,3) == 4
    assert binomial_Coeff(3,2) == 3
