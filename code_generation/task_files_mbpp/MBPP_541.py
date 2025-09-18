# MBPP/541
### Completion
def check_abundant(n):
    if n < 1:
        return False
    
    # Calculate the sum of proper divisors
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum of divisors is greater than the number
    return sum_of_divisors > n

# Test the function with the provided assertion
assert check_abundant(12) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_abundant(12) == True
    assert check_abundant(15) == False
    assert check_abundant(18) == True
