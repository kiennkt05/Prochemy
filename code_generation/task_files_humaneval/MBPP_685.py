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
    prime_sum = 0
    for number in range(2, n + 1):
        if is_prime(number):
            prime_sum += number
    return prime_sum

# Test the function with the provided assertion
assert sum_Of_Primes(10) == 17

# Additional test cases (optional)
print(sum_Of_Primes(10))  # Output: 17
print(sum_Of_Primes(20))  # Output: 77 (2 + 3 + 5 + 7 + 11 + 13 + 17 + 19)
print(sum_Of_Primes(1))   # Output: 0 (no primes)
print(sum_Of_Primes(2))   # Output: 2 (only prime is 2)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Of_Primes(10) == 17
    assert sum_Of_Primes(20) == 77
    assert sum_Of_Primes(5) == 10
