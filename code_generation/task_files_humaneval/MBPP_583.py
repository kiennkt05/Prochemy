# MBPP/583
### Completion
def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def catalan_number(n):
    """Calculate the nth Catalan number."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Using the formula C(n) = (2n)! / ((n + 1)! * n!)
    num = factorial(2 * n)
    denom = factorial(n + 1) * factorial(n)
    
    return num // denom  # Use integer division

# Test the function with the provided test case
assert catalan_number(10) == 16796

# If you want to see the output for other values, you can uncomment the following lines:
# print(catalan_number(0))  # Output: 1
# print(catalan_number(1))  # Output: 1
# print(catalan_number(2))  # Output: 2
# print(catalan_number(3))  # Output: 5
# print(catalan_number(4))  # Output: 14
# print(catalan_number(5))  # Output: 42
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429
