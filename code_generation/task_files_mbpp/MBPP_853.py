# MBPP/853
### Completion
def sum_of_odd_factors(n):
    odd_factors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:  # Check if i is a factor and odd
            odd_factors_sum += i
    return odd_factors_sum

# Test the function with the provided assertion
assert sum_of_odd_factors(30) == 24
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_odd_Factors(30) == 24
    assert sum_of_odd_Factors(18) == 13
    assert sum_of_odd_Factors(2) == 1
