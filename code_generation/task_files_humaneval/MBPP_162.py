# MBPP/162
### Completion
def sum_series(n):
    """
    Calculate the sum of the series n + (n-2) + (n-4) + ... until the term is <= 0.
    
    Parameters:
    n (int): The starting positive integer.
    
    Returns:
    int: The sum of the series.
    """
    total_sum = 0  # Initialize the sum
    current = n    # Start with n
    
    # Loop until current is greater than 0
    while current > 0:
        total_sum += current  # Add the current term to the sum
        current -= 2          # Decrease current by 2
    
    return total_sum  # Return the final sum

# Test case
assert sum_series(6) == 12  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_series(6)==12
    assert sum_series(10)==30
    assert sum_series(9)==25
