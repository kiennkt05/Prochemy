# MBPP/876
### Completion
def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the Least Common Multiple (LCM) of two positive integers."""
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers.")
    return abs(a * b) // gcd(a, b)

# Test case
assert lcm(4, 6) == 12

# Additional test cases for verification
assert lcm(15, 20) == 60
assert lcm(7, 5) == 35
assert lcm(1, 10) == 10
assert lcm(9, 28) == 252

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lcm(4,6) == 12
    assert lcm(15,17) == 255
    assert lcm(2,6) == 6
