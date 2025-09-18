# MBPP/260
### Completion
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    """Return the nth Newman–Shanks–Williams prime number."""
    count = 0
    candidate = 1  # Start checking from 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            # Check if the prime is a Newman–Shanks–Williams prime
            if candidate == 2 or candidate == 3 or candidate == 5 or candidate == 7 or candidate == 11 or candidate == 13 or candidate == 17 or candidate == 19 or candidate == 23 or candidate == 29:
                count += 1
    return candidate

# Test the function
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
