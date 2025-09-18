# MBPP/687
### Completion
def recur_gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using recursion.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The GCD of a and b.
    """
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: call recur_gcd with b and the remainder of a divided by b
    return recur_gcd(b, a % b)

# Test case
assert recur_gcd(12, 14) == 2

# Additional test cases for verification
assert recur_gcd(48, 18) == 6
assert recur_gcd(101, 10) == 1
assert recur_gcd(56, 98) == 14
assert recur_gcd(0, 5) == 5  # GCD of 0 and any number is the number itself
assert recur_gcd(5, 0) == 5  # GCD of any number and 0 is the number itself

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert recur_gcd(12,14) == 2
    assert recur_gcd(13,17) == 1
    assert recur_gcd(9, 3) == 3
