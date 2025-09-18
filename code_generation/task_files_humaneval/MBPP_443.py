# MBPP/443
### Completion
def largest_neg(numbers):
    """
    Function to find the largest negative number in a given list of numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int or None: The largest negative number if found, otherwise None.
    """
    largest_negative = None  # Initialize to None to indicate no negative number found yet
    
    for num in numbers:
        if num < 0:  # Check if the number is negative
            if largest_negative is None or num > largest_negative:
                largest_negative = num  # Update largest_negative if current num is larger
    
    return largest_negative  # Return the largest negative number found

# Test case
assert largest_neg([1, 2, 3, -4, -6]) == -6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_neg([1,2,3,-4,-6]) == -6
    assert largest_neg([1,2,3,-8,-9]) == -9
    assert largest_neg([1,2,3,4,-1]) == -1
