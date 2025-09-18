# MBPP/329
### Completion
def neg_count(numbers):
    """
    Count the number of negative numbers in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The count of negative numbers in the list.
    """
    count = 0  # Initialize counter for negative numbers
    for number in numbers:
        if number < 0:  # Check if the number is negative
            count += 1  # Increment the counter if negative
    return count  # Return the total count of negative numbers

# Test case
assert neg_count([-1, -2, 3, -4, -5]) == 4  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert neg_count([-1,-2,3,-4,-5]) == 4
    assert neg_count([1,2,3]) == 0
    assert neg_count([1,2,-3,-10,20]) == 2
