# MBPP/191
### Completion
def check_monthnumber(month_name):
    """
    Check if the given month name contains 30 days.

    Args:
    month_name (str): The name of the month to check.

    Returns:
    bool: True if the month has 30 days, False otherwise.
    """
    # List of months that have 30 days
    months_with_30_days = ["April", "June", "September", "November"]
    
    # Check if the month_name is in the list
    return month_name in months_with_30_days

# Test case
assert check_monthnumber("February") == False  # February does not have 30 days
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumber("February")==False
    assert check_monthnumber("June")==True
    assert check_monthnumber("April")==True
