# MBPP/926
### Completion
import math

def rencontres_number(n, k):
    # Check if n is even and n >= 2k
    if n % 2 != 0 or n < 2 * k:
        return 0
    
    # Calculate the factorials
    n_factorial = math.factorial(n)
    k_factorial = math.factorial(k)
    n_minus_2k_factorial = math.factorial(n - 2 * k)
    
    # Calculate the rencontres number using the formula
    result = n_factorial // (2**k * k_factorial * n_minus_2k_factorial)
    
    return result

# Test case
assert rencontres_number(7, 2) == 924  # This should raise no assertion error if the function is correct
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rencontres_number(7, 2) == 924
    assert rencontres_number(3, 0) == 2
    assert rencontres_number(3, 1) == 3
