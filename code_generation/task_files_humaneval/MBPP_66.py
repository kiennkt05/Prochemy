# MBPP/66
### Completion
def pos_count(numbers):
    """
    Count the number of positive numbers in a given list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The count of positive integers in the list.
    """
    count = 0  # Initialize the counter for positive numbers
    for number in numbers:
        if number > 0:  # Check if the number is positive
            count += 1  # Increment the counter if the number is positive
    return count  # Return the total count of positive numbers

# Test case
assert pos_count([1, -2, 3, -4]) == 2  # There are two positive numbers: 1 and 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4
