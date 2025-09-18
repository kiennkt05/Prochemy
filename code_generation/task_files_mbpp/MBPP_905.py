# MBPP/905
### Completion
import math

def sum_of_square(n):
    # Calculate the binomial coefficient C(2n, n)
    return math.comb(2 * n, n)

# Test the function with the provided assertion
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
