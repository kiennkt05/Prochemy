# MBPP/212
### Completion
def fourth_Power_Sum(n):
    """
    Calculate the sum of the fourth powers of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    int: The sum of the fourth powers of the first n natural numbers.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 4  # Calculate the fourth power and add to the total sum
    return total_sum

# Test the function with the provided test case
assert fourth_Power_Sum(2) == 17, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fourth_Power_Sum(2) == 17
    assert fourth_Power_Sum(4) == 354
    assert fourth_Power_Sum(6) == 2275
