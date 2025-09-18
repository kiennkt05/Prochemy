# MBPP/655
### Completion
def fifth_Power_Sum(n):
    """
    Calculate the sum of the fifth power of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    int: The sum of the fifth powers of the first n natural numbers.
    """
    # Calculate the sum of the fifth powers
    total_sum = sum(i ** 5 for i in range(1, n + 1))
    return total_sum

# Test case
assert fifth_Power_Sum(2) == 33  # 1^5 + 2^5 = 1 + 32 = 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fifth_Power_Sum(2) == 33
    assert fifth_Power_Sum(4) == 1300
    assert fifth_Power_Sum(3) == 276
