# MBPP/336
### Completion
def check_monthnum(month_name):
    """
    Check if the given month name contains 28 days.
    
    Args:
    month_name (str): The name of the month to check.
    
    Returns:
    bool: True if the month has 28 days, False otherwise.
    """
    # Normalize the month name to lowercase for case-insensitive comparison
    month_name = month_name.lower()
    
    # Check if the month is February
    if month_name == "february":
        return True
    else:
        return False

# Test case
assert check_monthnum("February") == True
assert check_monthnum("January") == False
assert check_monthnum("March") == False
assert check_monthnum("April") == False
assert check_monthnum("May") == False
assert check_monthnum("June") == False
assert check_monthnum("July") == False
assert check_monthnum("August") == False
assert check_monthnum("September") == False
assert check_monthnum("October") == False
assert check_monthnum("November") == False
assert check_monthnum("December") == False

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnum("February")==True
    assert check_monthnum("January")==False
    assert check_monthnum("March")==False
