# MBPP/164
### Completion
def sum_of_divisors(n):
    """Calculate the sum of all divisors of n."""
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def areEquivalent(num1, num2):
    """Check if the sum of divisors of num1 and num2 are the same."""
    return sum_of_divisors(num1) == sum_of_divisors(num2)

# Test the function with the provided assertion
assert areEquivalent(36, 57) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert areEquivalent(36,57) == False
    assert areEquivalent(2,4) == False
    assert areEquivalent(23,47) == True
