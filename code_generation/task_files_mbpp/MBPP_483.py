# MBPP/483
### Completion
def first_Factorial_Divisible_Number(x):
    import math
    
    n = 1
    while True:
        factorial = math.factorial(n)
        if factorial % x == 0:
            return n
        n += 1

# Test the function with the provided assertion
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
