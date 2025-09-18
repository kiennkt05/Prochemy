# MBPP/935
### Completion
def series_sum(n):
    return sum(i**2 for i in range(1, n + 1))

# Test the function with the provided assertion
assert series_sum(6) == 91
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert series_sum(6)==91
    assert series_sum(7)==140
    assert series_sum(12)==650
