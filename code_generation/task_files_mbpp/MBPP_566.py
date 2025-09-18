# MBPP/566
### Completion
def sum_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return sum(int(digit) for digit in str(n))

# Test the function with the provided assertion
assert sum_digits(345) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_digits(345)==12
    assert sum_digits(12)==3
    assert sum_digits(97)==16
