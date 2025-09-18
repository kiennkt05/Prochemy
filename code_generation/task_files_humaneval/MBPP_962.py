# MBPP/962
### Completion
def sum_Even(l, r):
    """
    Calculate the sum of all even natural numbers in the range [l, r].

    Parameters:
    l (int): The lower bound of the range (inclusive).
    r (int): The upper bound of the range (inclusive).

    Returns:
    int: The sum of all even natural numbers in the specified range.
    """
    total_sum = 0
    for number in range(l, r + 1):
        if number % 2 == 0:  # Check if the number is even
            total_sum += number  # Add to the total sum if it's even
    return total_sum

# Test case
assert sum_Even(2, 5) == 6  # 2 + 4 = 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_Even(2,5) == 6
    assert sum_Even(3,8) == 18
    assert sum_Even(4,6) == 10
