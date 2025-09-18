# MBPP/248
### Completion
def harmonic_sum(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum(1 / i for i in range(1, n))

# Test the function with the provided assertion
assert harmonic_sum(7) == 2.5928571428571425
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert harmonic_sum(7) == 2.5928571428571425
    assert harmonic_sum(4) == 2.083333333333333
    assert harmonic_sum(19) == 3.547739657143682
