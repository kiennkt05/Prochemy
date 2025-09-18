# MBPP/697
### Completion
def count_even(numbers):
    """
    Count the number of even elements in the given list using a lambda function.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The count of even integers in the list.
    """
    # Use filter with a lambda function to find even numbers and count them
    return len(list(filter(lambda x: x % 2 == 0, numbers)))

# Test case
assert count_even([1, 2, 3, 5, 7, 8, 9, 10]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_even([1, 2, 3, 5, 7, 8, 9, 10])==3
    assert count_even([10,15,14,13,-18,12,-20])==5
    assert count_even([1, 2, 4, 8, 9])==3
