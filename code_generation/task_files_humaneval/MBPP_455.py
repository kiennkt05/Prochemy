# MBPP/455
### Completion
def check_monthnumb_number(month: int) -> bool:
    """
    Check if the given month number has 31 days.

    Parameters:
    month (int): The month number (1-12).

    Returns:
    bool: True if the month has 31 days, False otherwise.
    """
    # List of months that have 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    
    # Check if the month number is valid and in the list
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    
    return month in months_with_31_days

# Test case
assert check_monthnumb_number(5) == True  # May has 31 days
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False
