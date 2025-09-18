# MBPP/714
### Completion
def count_Fac(n):
    """
    Count the number of distinct prime factors of a given number n.

    Parameters:
    n (int): The number to factor.

    Returns:
    int: The count of distinct prime factors.
    """
    if n <= 1:
        return 0  # No prime factors for numbers less than or equal to 1

    distinct_prime_factors = set()  # Use a set to store distinct prime factors

    # Check for number of 2s that divide n
    while n % 2 == 0:
        distinct_prime_factors.add(2)
        n //= 2

    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            distinct_prime_factors.add(i)
            n //= i

    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        distinct_prime_factors.add(n)

    return len(distinct_prime_factors)

# Test the function with the provided test case
assert count_Fac(24) == 3  # 24 = 2^3 * 3^1, distinct primes are 2 and 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Fac(24) == 3
    assert count_Fac(12) == 2
    assert count_Fac(4) == 1
