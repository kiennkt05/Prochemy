# MBPP/28
### Completion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_Coeff(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# Test the function
assert binomial_Coeff(5, 2) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binomial_Coeff(5,2) == 10
    assert binomial_Coeff(4,3) == 4
    assert binomial_Coeff(3,2) == 3
