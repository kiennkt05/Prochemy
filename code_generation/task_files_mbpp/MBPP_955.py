# MBPP/955
### Completion
def is_abundant(n):
    if n < 1:
        return False
    
    # Calculate the sum of proper divisors
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum of divisors is greater than the number
    return sum_of_divisors > n

# Test the function with the provided assertion
assert is_abundant(12) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_abundant(12)==True
    assert is_abundant(13)==False
    assert is_abundant(9)==False
