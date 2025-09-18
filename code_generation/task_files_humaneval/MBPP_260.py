# MBPP/260
### Completion
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def newman_prime(n):
    """Find the nth Newman–Shanks–Williams prime number."""
    count = 0  # Count of Newman–Shanks–Williams primes found
    p = 2      # Start checking for prime indices from 2
    newman_primes = []  # List to store the Newman–Shanks–Williams primes

    while count < n:
        if is_prime(p):
            # Calculate the Newman–Shanks–Williams prime
            newman_candidate = (1 << p) - 1  # This is 2^p - 1
            if is_prime(newman_candidate):
                newman_primes.append(newman_candidate)
                count += 1
        p += 1  # Move to the next number to check for primality

    return newman_primes[-1]  # Return the nth Newman–Shanks–Williams prime

# Test case
assert newman_prime(3) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert newman_prime(3) == 7 
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41
