# MBPP/762
### Completion
def check_monthnumber_number(month: int) -> bool:
    """
    Check if the given month number has 30 days.

    Parameters:
    month (int): The month number (1 for January, 2 for February, ..., 12 for December).

    Returns:
    bool: True if the month has 30 days, False otherwise.
    """
    # List of month numbers that have 30 days
    months_with_30_days = {4, 6, 9, 11}
    
    # Check if the provided month number is in the set of months with 30 days
    return month in months_with_30_days

# Test case
assert check_monthnumber_number(6) == True  # June has 30 days
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False
