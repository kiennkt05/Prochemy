# MBPP/258
### Completion
def count_odd(numbers):
    """
    Count the number of odd elements in the given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The count of odd integers in the list.
    """
    # Use filter with a lambda function to find odd numbers and count them
    return len(list(filter(lambda x: x % 2 != 0, numbers)))

# Test case
assert count_odd([1, 2, 3, 5, 7, 8, 10]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_odd([1, 2, 3, 5, 7, 8, 10])==4
    assert count_odd([10,15,14,13,-18,12,-20])==2
    assert count_odd([1, 2, 4, 8, 9])==2
