# MBPP/657
### Completion
import math

def first_Digit(n):
    # Calculate the factorial of n
    factorial_value = math.factorial(n)
    # Convert the factorial to string and get the first character
    first_digit = str(factorial_value)[0]
    # Convert the first character back to an integer
    return int(first_digit)

# Test the function with the provided assertion
assert first_Digit(5) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Digit(5) == 1
    assert first_Digit(10) == 3
    assert first_Digit(7) == 5
