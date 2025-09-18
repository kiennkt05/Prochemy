# MBPP/866
### Completion
def check_monthnumb(month_name):
    """
    Check if the given month name contains 31 days.

    Args:
    month_name (str): The name of the month to check.

    Returns:
    bool: True if the month has 31 days, False otherwise.
    """
    # List of months that have 31 days
    months_with_31_days = [
        "January", "March", "May", "July", 
        "August", "October", "December"
    ]
    
    # Check if the month name is in the list
    return month_name in months_with_31_days

# Test case
assert check_monthnumb("February") == False  # February does not have 31 days
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumb("February")==False
    assert check_monthnumb("January")==True
    assert check_monthnumb("March")==True
