# MBPP/274
### Completion
def even_binomial_Coeff_Sum(n):
    return 2 ** (n - 1)

# Test the function with the provided assertion
assert even_binomial_Coeff_Sum(4) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2
