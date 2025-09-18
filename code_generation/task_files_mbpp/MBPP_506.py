# MBPP/506
### Completion
import math

def permutation_coefficient(n, k):
    if k > n:
        return 0  # If k is greater than n, permutations are not possible
    return math.factorial(n) // math.factorial(n - k)

# Test the function with the provided assertion
assert permutation_coefficient(10, 2) == 90
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert permutation_coefficient(10, 2) == 90
    assert permutation_coefficient(10, 3) == 720
    assert permutation_coefficient(10, 1) == 10
