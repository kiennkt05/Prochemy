# MBPP/483
### Completion
def first_Factorial_Divisible_Number(x):
    """
    Find the first natural number n such that n! is divisible by x.
    
    Parameters:
    x (int): The number to check divisibility against.
    
    Returns:
    int: The first natural number whose factorial is divisible by x.
    """
    if x <= 0:
        raise ValueError("x must be a positive integer.")
    
    factorial = 1
    n = 1
    
    while True:
        factorial *= n  # Calculate n!
        if factorial % x == 0:  # Check if n! is divisible by x
            return n
        n += 1  # Move to the next natural number

# Test case
assert first_Factorial_Divisible_Number(10) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Factorial_Divisible_Number(10) == 5
    assert first_Factorial_Divisible_Number(15) == 5
    assert first_Factorial_Divisible_Number(5) == 4
