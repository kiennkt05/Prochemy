# MBPP/47
### Completion
def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_Last_Digit(a, b):
    """
    Compute the last digit of the division of factorial of b by factorial of a.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The last digit of (b! / a!).
    """
    if a > b:
        raise ValueError("a must be less than or equal to b.")
    
    # Calculate factorials
    factorial_a = factorial(a)
    factorial_b = factorial(b)
    
    # Perform division
    division_result = factorial_b // factorial_a  # Use integer division
    
    # Get the last digit
    last_digit = division_result % 10
    
    return last_digit

# Test case
assert compute_Last_Digit(2, 4) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert compute_Last_Digit(2,4) == 2
    assert compute_Last_Digit(6,8) == 6
    assert compute_Last_Digit(1,2) == 2
