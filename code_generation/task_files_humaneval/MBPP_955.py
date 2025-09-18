# MBPP/955
### Completion
def is_abundant(n):
    """
    Determine if a number is abundant.
    
    A number is abundant if the sum of its proper divisors is greater than the number itself.
    
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
            
    # Check if the sum of proper divisors is greater than the number
    return proper_divisors_sum > n

# Test case
assert is_abundant(12) == True  # 12 is an abundant number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_abundant(12)==True
    assert is_abundant(13)==False
    assert is_abundant(9)==False
