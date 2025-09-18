# MBPP/498
### Completion
def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two positive integers using the Euclidean algorithm.

    Parameters:
    a (int): The first positive integer.
    b (int): The second positive integer.

    Returns:
    int: The GCD of the two integers.
    """
    while b != 0:
        a, b = b, a % b  # Update a and b
    return a

# Test case
assert gcd(12, 17) == 1  # 12 and 17 are coprime, so their GCD is 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert gcd(12, 17) == 1
    assert gcd(4,6) == 2
    assert gcd(2,9) == 1
