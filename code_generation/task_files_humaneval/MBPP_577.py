# MBPP/577
### Completion
def last_Digit_Factorial(n):
    """
    Calculate the last digit of the factorial of a given number n.
    
    Parameters:
    n (int): The number to calculate the factorial for.
    
    Returns:
    int: The last digit of the factorial of n.
    """
    # Handle cases for n < 0
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # For n = 0 or n = 1, factorial is 1
    if n == 0 or n == 1:
        return 1
    
    # For n = 2, 3, 4, we can calculate the factorial directly
    if n <= 4:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial % 10  # Return the last digit
    
    # For n >= 5, the last digit of factorial is always 0
    return 0

# Test case
assert last_Digit_Factorial(4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0
