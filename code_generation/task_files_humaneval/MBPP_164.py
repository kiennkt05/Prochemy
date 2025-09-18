# MBPP/164
### Completion
def sum_of_divisors(n):
    """Calculate the sum of all divisors of a given number n."""
    if n < 1:
        return 0  # No divisors for non-positive integers
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def areEquivalent(a, b):
    """Check if the sum of divisors of a and b are the same."""
    sum_a = sum_of_divisors(a)
    sum_b = sum_of_divisors(b)
    return sum_a == sum_b

# Test case
assert areEquivalent(36, 57) == False  # 36 has divisors sum of 91, 57 has divisors sum of 1 + 3 + 19 + 57 = 80
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert areEquivalent(36,57) == False
    assert areEquivalent(2,4) == False
    assert areEquivalent(23,47) == True
