# MBPP/692
### Completion
def last_Two_Digits(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    
    return factorial % 100

# Test the function with the provided assertion
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
