# MBPP/402
### Completion
def factorial_mod(n, p):
    """Compute factorial % p for all numbers from 0 to n."""
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p
    return fact

def ncr_modp(n, r, p):
    """Compute nCr % p."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Precompute all factorials % p
    fact = factorial_mod(n, p)
    
    # Compute nCr % p using the formula
    numerator = fact[n]
    denominator = (fact[r] * fact[n - r]) % p
    
    # Compute the modular inverse of the denominator
    denominator_inv = pow(denominator, p - 2, p)
    
    # Return the result
    return (numerator * denominator_inv) % p

# Test the function with the provided assertion
assert ncr_modp(10, 2, 13) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ncr_modp(10,2,13)==6
    assert ncr_modp(15,12,43)==25
    assert ncr_modp(17,9,18)==10
