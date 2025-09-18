# MBPP/952
### Completion
def factorial_mod(n, p):
    """Compute factorials % p for all numbers from 0 to n."""
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
    return fact

def mod_inverse(a, p):
    """Compute the modular inverse of a under modulo p using Fermat's Little Theorem."""
    return pow(a, p - 2, p)

def nCr_mod_p(n, r, p):
    """Compute nCr % p."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Precompute all factorials % p
    fact = factorial_mod(n, p)
    
    # Compute nCr % p
    numerator = fact[n]
    denominator = (fact[r] * fact[n - r]) % p
    
    # Use modular inverse to compute the result
    result = (numerator * mod_inverse(denominator, p)) % p
    return result

# Test case
assert nCr_mod_p(10, 2, 13) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert nCr_mod_p(10, 2, 13) == 6
    assert nCr_mod_p(11, 3, 14) == 11
    assert nCr_mod_p(18, 14, 19) == 1
