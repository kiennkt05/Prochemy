# MBPP/770
### Completion
def odd_Num_Sum(n):
    """
    Calculate the sum of the fourth power of the first n odd natural numbers.

    Parameters:
    n (int): The number of odd natural numbers to consider.

    Returns:
    int: The sum of the fourth powers of the first n odd natural numbers.
    """
    total_sum = 0
    for i in range(n):
        odd_number = 2 * i + 1  # Generate the i-th odd natural number
        total_sum += odd_number ** 4  # Add the fourth power of the odd number to the total sum
    return total_sum

# Test case
assert odd_Num_Sum(2) == 82  # 1^4 + 3^4 = 1 + 81 = 82
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Num_Sum(2) == 82
    assert odd_Num_Sum(3) == 707
    assert odd_Num_Sum(4) == 3108
