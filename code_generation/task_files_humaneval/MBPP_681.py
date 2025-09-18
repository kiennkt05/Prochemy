# MBPP/681
### Completion
def smallest_Divisor(n):
    """
    Find the smallest prime divisor of a given number n.
    
    Parameters:
    n (int): The number to find the smallest prime divisor for.
    
    Returns:
    int: The smallest prime divisor of n, or None if n < 2.
    """
    if n < 2:
        return None  # No prime divisors for numbers less than 2
    
    # Check for the smallest prime divisor starting from 2
    if n % 2 == 0:
        return 2  # 2 is the smallest prime number
    
    # Check for odd divisors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i  # Return the first found prime divisor
    
    return n  # If no divisors found, n is prime

# Test case
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
