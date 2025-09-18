# MBPP/435
### Completion
def last_Digit(number):
    """
    This function returns the last digit of the given integer number.
    
    Parameters:
    number (int): The integer from which to extract the last digit.
    
    Returns:
    int: The last digit of the number.
    """
    return abs(number) % 10  # Use abs to handle negative numbers

# Test case
assert last_Digit(123) == 3  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0
