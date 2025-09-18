# MBPP/133
### Completion
def sum_negativenum(numbers):
    """
    Calculate the sum of negative numbers in a given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The sum of negative numbers in the list.
    """
    # Filter the negative numbers using a lambda function and sum them
    return sum(filter(lambda x: x < 0, numbers))

# Test the function with the provided test case
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32

# You can add more test cases to validate the function
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
    assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52
    assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894
