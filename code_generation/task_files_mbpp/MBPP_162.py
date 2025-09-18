# MBPP/162
### Completion
def sum_series(n):
    total = 0
    while n > 0:
        total += n
        n -= 2
    return total

# Test the function with the provided assertion
assert sum_series(6) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_series(6)==12
    assert sum_series(10)==30
    assert sum_series(9)==25
