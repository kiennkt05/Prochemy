# MBPP/3
### Completion
def is_not_prime(n):
    if n < 2:
        return True  # Numbers less than 2 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True  # Found a divisor, so n is not prime
    return False  # No divisors found, so n is prime

# Test case
assert is_not_prime(2) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_not_prime(2) == False
    assert is_not_prime(10) == True
    assert is_not_prime(35) == True
