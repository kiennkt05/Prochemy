# MBPP/952
### Completion
def factorial_mod(n, p):
    """Compute n! % p for n >= 0."""
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % p
    return result

def mod_inverse(a, p):
    """Compute the modular inverse of a under modulo p using Fermat's Little Theorem."""
    return pow(a, p - 2, p)

def nCr_mod_p(n, r, p):
    """Compute nCr % p."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Calculate n!, r!, and (n-r)!
    num = factorial_mod(n, p)
    denom = (factorial_mod(r, p) * factorial_mod(n - r, p)) % p
    
    # Calculate the modular inverse of denom
    denom_inv = mod_inverse(denom, p)
    
    # Calculate nCr % p
    return (num * denom_inv) % p

# Test the function with the provided assertion
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
