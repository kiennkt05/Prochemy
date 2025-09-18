# MBPP/256
### Completion
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_Primes_nums(n):
    """Count the number of prime numbers less than a given non-negative number n."""
    if n <= 2:
        return 0  # There are no prime numbers less than 2
    
    prime_count = 0
    for number in range(2, n):
        if is_prime(number):
            prime_count += 1
            
    return prime_count

# Test case
assert count_Primes_nums(5) == 2  # The prime numbers less than 5 are 2 and 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25
