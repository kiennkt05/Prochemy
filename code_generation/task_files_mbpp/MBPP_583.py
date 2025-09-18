# MBPP/583
### Completion
import math

def catalan_number(n):
    # Calculate the nth Catalan number using the formula
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

# Test the function
assert catalan_number(10) == 16796
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429
