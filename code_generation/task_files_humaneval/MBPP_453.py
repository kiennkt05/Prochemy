# MBPP/453
### Completion
def sumofFactors(n):
    """
    Calculate the sum of even factors of a given number n.

    Parameters:
    n (int): The number for which to find the sum of even factors.

    Returns:
    int: The sum of even factors of n.
    """
    even_factors_sum = 0
    
    # Loop through all numbers from 1 to n to find factors
    for i in range(1, n + 1):
        if n % i == 0:  # Check if i is a factor of n
            if i % 2 == 0:  # Check if the factor is even
                even_factors_sum += i  # Add to the sum if it's even

    return even_factors_sum

# Test case
assert sumofFactors(18) == 26  # 2 + 6 + 18 = 26
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8
