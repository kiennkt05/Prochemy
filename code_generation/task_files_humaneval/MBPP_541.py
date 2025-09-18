# MBPP/541
### Completion
def check_abundant(n):
    """
    Check if a number is abundant.
    
    An abundant number is a number for which the sum of its proper divisors
    is greater than the number itself.
    
    Parameters:
    n (int): The number to check for abundance.
    
    Returns:
    bool: True if the number is abundant, False otherwise.
    """
    if n < 1:
        return False  # Abundant numbers are positive integers
    
    # Calculate the sum of proper divisors
    proper_divisors_sum = 0
    for i in range(1, n // 2 + 1):  # Check divisors up to n/2
        if n % i == 0:
            proper_divisors_sum += i
            
    # Check if the sum of proper divisors is greater than n
    return proper_divisors_sum > n

# Test case
assert check_abundant(12) == True  # 12 is an abundant number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_abundant(12) == True
    assert check_abundant(15) == False
    assert check_abundant(18) == True
