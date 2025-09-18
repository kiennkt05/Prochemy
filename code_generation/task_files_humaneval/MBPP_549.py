# MBPP/549
### Completion
def odd_Num_Sum(n):
    """
    Calculate the sum of the fifth power of the first n odd natural numbers.

    Parameters:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of the fifth powers of the first n odd natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        odd_number = 2 * i - 1  # Calculate the i-th odd number
        total_sum += odd_number ** 5  # Add the fifth power of the odd number to the total sum
    return total_sum

# Test case
assert odd_Num_Sum(1) == 1  # The first odd number is 1, and 1^5 = 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Num_Sum(1) == 1
    assert odd_Num_Sum(2) == 244
    assert odd_Num_Sum(3) == 3369
