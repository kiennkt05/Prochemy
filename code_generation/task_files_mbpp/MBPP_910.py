# MBPP/910
### Completion
def check_date(day, month, year):
    # Check if the year is a valid integer
    if not isinstance(year, int) or year < 1:
        return False
    
    # Check if the month is valid
    if month < 1 or month > 12:
        return False
    
    # Days in each month
    days_in_month = [31, 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the day is valid
    if day < 1 or day > days_in_month[month - 1]:
        return False
    
    return True

# Test the function
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
