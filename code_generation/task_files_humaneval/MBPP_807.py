# MBPP/807
### Completion
def first_odd(numbers):
    """
    This function returns the first odd number in a given list of numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int or None: The first odd number found in the list, or None if no odd number exists.
    """
    for number in numbers:
        if number % 2 != 0:  # Check if the number is odd
            return number  # Return the first odd number found
    return None  # Return None if no odd number is found

# Test case
assert first_odd([1, 3, 5]) == 1  # This should pass as 1 is the first odd number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_odd([1,3,5]) == 1
    assert first_odd([2,4,1,3]) == 1
    assert first_odd ([8,9,1]) == 9
