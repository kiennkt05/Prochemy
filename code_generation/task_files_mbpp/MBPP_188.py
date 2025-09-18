# MBPP/188
### Completion
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return the prime factors of n along with their exponents."""
    factors = {}
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
    return factors

def prod_Square(n):
    """Check if the number can be represented as a product of two squares."""
    if n < 0:
        return False  # Negative numbers cannot be expressed as a product of two squares
    factors = prime_factors(n)
    for prime, exponent in factors.items():
        if prime % 4 == 3 and exponent % 2 != 0:
            return False
    return True

# Test the function with the provided assertion
assert prod_Square(25) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert prod_Square(25) == False
    assert prod_Square(30) == False
    assert prod_Square(16) == True
