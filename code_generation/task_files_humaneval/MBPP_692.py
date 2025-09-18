# MBPP/692
### Completion
def last_Two_Digits(n):
    """
    Calculate the last two digits of the factorial of a given number n.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The last two digits of n! (factorial of n).
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Initialize factorial result
    factorial = 1
    
    # Calculate factorial
    for i in range(2, n + 1):
        factorial *= i
    
    # Get the last two digits
    last_two_digits = factorial % 100
    
    return last_two_digits

# Test case
assert last_Two_Digits(7) == 40
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_Two_Digits(7) == 40
    assert last_Two_Digits(5) == 20
    assert last_Two_Digits(2) == 2
