# MBPP/853
### Completion
def sum_of_odd_factors(n):
    """
    Calculate the sum of all odd factors of a given number n.

    Parameters:
    n (int): The number for which to find the sum of odd factors.

    Returns:
    int: The sum of odd factors of n.
    """
    odd_factors_sum = 0
    
    # Loop through all numbers from 1 to n to find factors
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a factor of n
            if i % 2 != 0:  # Check if the factor is odd
                odd_factors_sum += i  # Add to the sum if it's odd

    return odd_factors_sum

# Test case
assert sum_of_odd_factors(30) == 24  # 1 + 3 + 5 + 15 = 24
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_of_odd_Factors(30) == 24
    assert sum_of_odd_Factors(18) == 13
    assert sum_of_odd_Factors(2) == 1
