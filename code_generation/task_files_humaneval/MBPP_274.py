# MBPP/274
### Completion
def even_binomial_Coeff_Sum(n):
    """
    Calculate the sum of binomial coefficients at even indices for a given n.
    
    Parameters:
    n (int): The upper index for the binomial coefficients.
    
    Returns:
    int: The sum of binomial coefficients at even indices.
    """
    # Using the formula derived from the binomial theorem
    return (2 ** n + 0) // 2

# Test case
assert even_binomial_Coeff_Sum(4) == 8

# Additional test cases
assert even_binomial_Coeff_Sum(0) == 1  # C(0, 0) = 1
assert even_binomial_Coeff_Sum(1) == 1  # C(1, 0) = 1
assert even_binomial_Coeff_Sum(2) == 2  # C(2, 0) + C(2, 2) = 1 + 1
assert even_binomial_Coeff_Sum(3) == 4  # C(3, 0) + C(3, 2) = 1 + 3
assert even_binomial_Coeff_Sum(5) == 16 # C(5, 0) + C(5, 2) + C(5, 4) = 1 + 10 + 5

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2
