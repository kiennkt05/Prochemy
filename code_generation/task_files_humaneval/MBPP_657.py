# MBPP/657
### Completion
import math

def first_Digit(n):
    """
    This function returns the first digit of the factorial of a given number n.
    
    Parameters:
    n (int): The number for which to calculate the factorial and find the first digit.
    
    Returns:
    int: The first digit of the factorial of n.
    """
    # Calculate the factorial using math.factorial
    factorial_value = math.factorial(n)
    
    # Convert the factorial to a string
    factorial_str = str(factorial_value)
    
    # Return the first character as an integer
    return int(factorial_str[0])

# Test case
assert first_Digit(5) == 1  # 5! = 120, first digit is 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Digit(5) == 1
    assert first_Digit(10) == 3
    assert first_Digit(7) == 5
