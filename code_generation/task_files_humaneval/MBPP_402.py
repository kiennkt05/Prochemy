# MBPP/402
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

def ncr_modp(n, r, p):
    """Compute nCr % p."""
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Calculate n!, r!, and (n-r)!
    num = factorial_mod(n, p)
    denom_r = factorial_mod(r, p)
    denom_n_r = factorial_mod(n - r, p)
    
    # Calculate nCr % p
    denom = (denom_r * denom_n_r) % p
    denom_inv = mod_inverse(denom, p)
    
    return (num * denom_inv) % p

# Test the function with the provided test case
assert ncr_modp(10, 2, 13) == 6

# You can add more test cases to validate the function
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ncr_modp(10,2,13)==6
    assert ncr_modp(15,12,43)==25
    assert ncr_modp(17,9,18)==10
