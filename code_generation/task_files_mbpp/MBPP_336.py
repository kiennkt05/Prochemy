# MBPP/336
### Completion
def check_monthnum(month_name):
    # Normalize the month name to lowercase for case-insensitive comparison
    month_name = month_name.lower()
    
    # Check if the month is February
    if month_name == "february":
        return True
    else:
        return False

# Test the function with the provided assertion
assert check_monthnum("February") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnum("February")==True
    assert check_monthnum("January")==False
    assert check_monthnum("March")==False
