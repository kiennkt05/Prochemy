# MBPP/931
### Completion
def sum_series(n):
    return sum(i**3 for i in range(1, n + 1))

# Test the function with the provided assertion
assert sum_series(7) == 784
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_series(7)==784
    assert sum_series(5)==225
    assert sum_series(15)==14400
