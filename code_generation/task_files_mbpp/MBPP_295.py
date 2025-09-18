# MBPP/295
### Completion
def sum_div(n):
    # Initialize the sum of divisors
    total = 0
    # Loop through all numbers from 1 to n//2 (inclusive)
    for i in range(1, n // 2 + 1):
        if n % i == 0:  # Check if i is a divisor of n
            total += i  # Add the divisor to the total
    return total

# Test the function with the provided assertion
assert sum_div(8) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1
