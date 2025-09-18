# MBPP/738
### Completion
def geometric_sum(n):
    if n <= 1:
        return 0  # If n is 1 or less, the sum is 0 since there are no terms.
    a = 1  # First term
    r = 0.5  # Common ratio
    num_terms = n - 1  # Number of terms
    return a * (1 - r**num_terms) / (1 - r)

# Test the function with the provided assertion
assert geometric_sum(7) == 1.9921875
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375
