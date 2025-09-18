# MBPP/295
### Completion
def sum_div(n):
    """
    Calculate the sum of all proper divisors of a given number n.

    Parameters:
    n (int): The number for which to find the sum of divisors.

    Returns:
    int: The sum of all proper divisors of n.
    """
    # Initialize the sum of divisors
    total = 0
    
    # Iterate through all numbers from 1 to n-1
    for i in range(1, n):
        if n % i == 0:  # Check if i is a divisor of n
            total += i  # Add the divisor to the total sum
            
    return total

# Test case
assert sum_div(8) == 7  # The divisors of 8 are 1, 2, 4; their sum is 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1
