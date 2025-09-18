# MBPP/32
### Completion
def max_Prime_Factors(n):
    # Initialize the largest prime factor
    largest_prime = -1
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, update n and largest_prime
        while n % i == 0:
            largest_prime = i
            n //= i
    
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        largest_prime = n
    
    return largest_prime

# Test case
assert max_Prime_Factors(15) == 5

# Additional test cases
assert max_Prime_Factors(28) == 7
assert max_Prime_Factors(13195) == 29
assert max_Prime_Factors(2) == 2
assert max_Prime_Factors(1) == -1  # 1 has no prime factors
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_Prime_Factors(15) == 5
    assert max_Prime_Factors(6) == 3
    assert max_Prime_Factors(2) == 2
