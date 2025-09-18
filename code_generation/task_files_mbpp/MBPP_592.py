# MBPP/592
### Completion
def sum_Of_product(n):
    # Calculate the sum of product of binomial coefficients
    return n * (2 ** (n - 1))

# Test the function with the provided assertion
assert sum_Of_product(3) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1
