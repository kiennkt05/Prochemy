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

def sum_of_prime_divisors(num):
    """Return the sum of all prime divisors of the given number."""
    prime_divisors = set()  # Use a set to avoid duplicate prime divisors
    for i in range(1, num + 1):
        if num % i == 0:  # Check if i is a divisor of num
            if is_prime(i):  # Check if the divisor is prime
                prime_divisors.add(i)  # Add to the set of prime divisors
    return sum(prime_divisors)  # Return the sum of prime divisors

# Test case
assert sum_of_prime_divisors(60) == 10  # 2 + 3 + 5 = 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Sum(60) == 10
    assert Sum(39) == 16
    assert Sum(40) == 7
