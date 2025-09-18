# MBPP/177
### Completion
import math

def answer(start, end):
    # Iterate through all pairs of distinct numbers in the range
    for a in range(start, end + 1):
        for b in range(a + 1, end + 1):  # Ensure b > a to maintain distinctness
            lcm = abs(a * b) // math.gcd(a, b)  # Calculate LCM using GCD
            if start <= lcm <= end:  # Check if LCM is within the range
                return (a, b)  # Return the first valid pair
    return None  # Return None if no valid pair is found

# Test case
assert answer(3, 8) == (3, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert answer(3,8) == (3,6)
    assert answer(2,6) == (2,4)
    assert answer(1,3) == (1,2)
