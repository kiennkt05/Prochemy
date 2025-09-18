# MBPP/797
### Completion
def sum_in_range(l, r):
    """
    Calculate the sum of all odd natural numbers in the range from l to r (inclusive).
    
    Parameters:
    l (int): The lower bound of the range.
    r (int): The upper bound of the range.
    
    Returns:
    int: The sum of all odd natural numbers in the specified range.
    """
    total_sum = 0
    for number in range(l, r + 1):
        if number % 2 != 0:  # Check if the number is odd
            total_sum += number  # Add to the total sum if it's odd
    return total_sum

# Test case
assert sum_in_range(2, 5) == 8  # 3 + 5 = 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_in_Range(2,5) == 8
    assert sum_in_Range(5,7) == 12
    assert sum_in_Range(7,13) == 40
