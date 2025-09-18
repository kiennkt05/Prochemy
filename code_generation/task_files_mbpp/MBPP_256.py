# MBPP/256
### Completion
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_Primes_nums(n):
    """Count the number of prime numbers less than a given non-negative number."""
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

# Test the function with the provided assertion
assert count_Primes_nums(5) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25
