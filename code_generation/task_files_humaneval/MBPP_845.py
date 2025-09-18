# MBPP/845
### Completion
import math

def find_Digits(n):
    """
    Calculate the number of digits in the factorial of a given number n.

    Parameters:
    n (int): The number for which to calculate the factorial and count digits.

    Returns:
    int: The number of digits in n!
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Calculate factorial
    factorial_value = math.factorial(n)
    
    # Count the number of digits
    num_digits = len(str(factorial_value))
    
    return num_digits

# Test case
assert find_Digits(7) == 4  # 7! = 5040, which has 4 digits
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Digits(7) == 4
    assert find_Digits(5) == 3
    assert find_Digits(4) == 2
