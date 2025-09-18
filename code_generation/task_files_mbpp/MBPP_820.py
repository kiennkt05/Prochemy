# MBPP/820
### Completion
def check_monthnum_number(month):
    """
    Check if the given month number contains 28 days.
    
    Args:
    month (int): The month number (1 for January, 2 for February, ..., 12 for December).
    
    Returns:
    bool: True if the month has 28 days, False otherwise.
    """
    # February is the only month that has 28 days in a non-leap year
    return month == 2

# Test the function with the provided assertion
assert check_monthnum_number(2) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnum_number(2)==True
    assert check_monthnum_number(1)==False
    assert check_monthnum_number(3)==False
