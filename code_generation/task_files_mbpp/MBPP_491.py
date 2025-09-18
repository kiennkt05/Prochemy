# MBPP/491
### Completion
def sum_gp(a, n, r):
    if r == 1:
        return a * n  # If the common ratio is 1, the series is just n times the first term
    return a * (r**n - 1) // (r - 1)

# Test the function with the provided assertion
assert sum_gp(1, 5, 2) == 31
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_gp(1,5,2)==31
    assert sum_gp(1,5,4)==341
    assert sum_gp(2,6,3)==728
