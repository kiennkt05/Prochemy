# MBPP/849
### Completion
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_divisors_sum(n):
    """Return the sum of all prime divisors of a given number."""
    prime_divisors = set()
    
    # Check for all numbers from 2 to n
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors.add(i)
    
    return sum(prime_divisors)

# Test the function
assert prime_divisors_sum(60) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Sum(60) == 10
    assert Sum(39) == 16
    assert Sum(40) == 7
