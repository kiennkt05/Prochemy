# MBPP/820
### Completion
def check_monthnum_number(month: int) -> bool:
    """
    Check if the given month number contains 28 days.
    
    Args:
    month (int): The month number (1-12).
    
    Returns:
    bool: True if the month has 28 days, False otherwise.
    """
    # Check if the month number is valid
    if month < 1 or month > 12:
        raise ValueError("Month number must be between 1 and 12.")
    
    # February is the only month with 28 days in a non-leap year
    return month == 2

# Test case
assert check_monthnum_number(2) == True  # February has 28 days
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnum_number(2)==True
    assert check_monthnum_number(1)==False
    assert check_monthnum_number(3)==False
