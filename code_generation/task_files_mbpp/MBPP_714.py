# MBPP/714
### Completion
def count_Fac(n):
    if n < 2:
        return 0
    
    distinct_prime_factors = set()
    
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

# Test the function with the provided assertion
assert count_Fac(24) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Fac(24) == 3
    assert count_Fac(12) == 2
    assert count_Fac(4) == 1
