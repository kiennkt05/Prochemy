# MBPP/47
### Completion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def compute_Last_Digit(a, b):
    if a > b:
        raise ValueError("a must be less than or equal to b")
    
    factorial_a = factorial(a)
    factorial_b = factorial(b)
    
    result = factorial_b // factorial_a  # Integer division
    last_digit = result % 10  # Get the last digit
    
    return last_digit

# Test the function with the provided assertion
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
