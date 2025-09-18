# MBPP/685
### Completion
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_Of_Primes(n):
    """Return the sum of all prime numbers between 1 and n."""
    return sum(num for num in range(2, n + 1) if is_prime(num))

# Test the function
assert sum_Of_Primes(10) == 17
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_Primes(10) == 17
    assert sum_Of_Primes(20) == 77
    assert sum_Of_Primes(5) == 10
