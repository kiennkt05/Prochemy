# MBPP/681
### Completion
def smallest_Divisor(n):
    if n <= 1:
        return None  # No prime divisors for numbers less than or equal to 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n  # If no divisors found, n is prime

# Test the function with the provided assertion
assert smallest_Divisor(10) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smallest_Divisor(10) == 2
    assert smallest_Divisor(25) == 5
    assert smallest_Divisor(31) == 31
