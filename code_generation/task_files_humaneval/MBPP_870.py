# MBPP/870
### Completion
def sum_positivenum(numbers):
    """
    Calculate the sum of positive numbers in a given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The sum of positive integers in the list.
    """
    # Filter positive numbers using a lambda function and sum them
    return sum(filter(lambda x: x > 0, numbers))

# Test the function with the provided test case
assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 48

# Additional test cases can be added to verify the function further
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==48
    assert sum_positivenum([10,15,-14,13,-18,12,-20])==50
    assert sum_positivenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==522
