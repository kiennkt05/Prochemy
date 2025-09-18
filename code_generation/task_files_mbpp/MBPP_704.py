# MBPP/704
### Completion
def harmonic_sum(n):
    if n < 1:
        return 0  # Return 0 for n <= 1 as there are no terms to sum
    return sum(1 / i for i in range(1, n))

# Test the function with the provided assertion
assert harmonic_sum(10) == 2.9289682539682538
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert harmonic_sum(10)==2.9289682539682538
    assert harmonic_sum(4)==2.083333333333333
    assert harmonic_sum(7)==2.5928571428571425 
