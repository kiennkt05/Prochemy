# MBPP/603
### Completion
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_up_to(n):
    """Return a list of prime numbers up to n."""
    return [i for i in range(2, n + 1) if is_prime(i)]

def get_ludic(n):
    """Return a list of lucid numbers less than or equal to n."""
    if n < 1:
        return []
    
    primes = get_primes_up_to(n)
    lucid_numbers = []
    
    for i in range(1, n + 1):
        # Check if i is divisible by any prime greater than i
        is_lucid = True
        for prime in primes:
            if prime > i:
                break
            if i % prime == 0:
                is_lucid = False
                break
        if is_lucid:
            lucid_numbers.append(i)
    
    return lucid_numbers

# Test case
assert get_ludic(10) == [1, 2, 3, 5, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
