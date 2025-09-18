# MBPP/910
### Completion
def check_date(day, month, year):
    """
    Validate a Gregorian date.
    
    Parameters:
    day (int): The day of the month.
    month (int): The month of the year (1-12).
    year (int): The year (positive integer).
    
    Returns:
    bool: True if the date is valid, False otherwise.
    """
    
    # Check if the year is a positive integer
    if year < 1:
        return False
    
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year and adjust February days
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  # February has 29 days in a leap year
    
    # Check if the day is valid for the given month
    if day < 1 or day > days_in_month[month - 1]:
        return False
    
    return True

# Test case
assert check_date(11, 11, 2002) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_date(11,11,2002)==True
    assert check_date(13,11,2002)==False
    assert check_date('11','11','2002')==True
