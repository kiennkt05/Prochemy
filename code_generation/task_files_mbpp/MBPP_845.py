# MBPP/845
### Completion
import math

def find_Digits(n):
    if n < 0:
        return 0  # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1  # 0! and 1! both equal 1, which has 1 digit

    # Calculate the number of digits in n!
    digits = 0
    for i in range(2, n + 1):
        digits += math.log10(i)
    
    return math.floor(digits) + 1

# Test the function with the provided assertion
assert find_Digits(7) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Digits(7) == 4
    assert find_Digits(5) == 3
    assert find_Digits(4) == 2
