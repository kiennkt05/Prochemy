# MBPP/498
### Completion
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function with the provided assertion
assert gcd(12, 17) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert gcd(12, 17) == 1
    assert gcd(4,6) == 2
    assert gcd(2,9) == 1
