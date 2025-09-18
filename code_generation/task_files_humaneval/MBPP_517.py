# MBPP/517
### Completion
def largest_pos(numbers):
    """
    Find the largest positive number in a given list of numbers.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int or None: The largest positive number if found, otherwise None.
    """
    largest = None  # Initialize largest as None

    for num in numbers:
        if num > 0:  # Check if the number is positive
            if largest is None or num > largest:  # Update largest if necessary
                largest = num

    return largest  # Return the largest positive number found

# Test case
assert largest_pos([1, 2, 3, 4, -1]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_pos([1,2,3,4,-1]) == 4
    assert largest_pos([0,1,2,-5,-1,6]) == 6
    assert largest_pos([0,0,1,0]) == 1
