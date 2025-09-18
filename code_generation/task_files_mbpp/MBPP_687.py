# MBPP/687
### Completion
def recur_gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: call recur_gcd with b and the remainder of a divided by b
    return recur_gcd(b, a % b)

# Test the function with the provided assertion
assert recur_gcd(12, 14) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert recur_gcd(12,14) == 2
    assert recur_gcd(13,17) == 1
    assert recur_gcd(9, 3) == 3
