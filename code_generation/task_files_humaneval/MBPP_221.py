# MBPP/221
### Completion
def first_even(numbers):
    """
    Find the first even number in a given list of numbers.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int or None: The first even number found in the list, or None if no even number exists.
    """
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            return number  # Return the first even number found
    return None  # Return None if no even number is found

# Test case
assert first_even([1, 3, 5, 7, 4, 1, 6, 8]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_even ([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert first_even([2, 3, 4]) == 2
    assert first_even([5, 6, 7]) == 6
