# MBPP/866
### Completion
def check_monthnumb(month_name):
    # List of months that have 31 days
    months_with_31_days = [
        "January", "March", "May", "July", 
        "August", "October", "December"
    ]
    
    # Check if the month name is in the list
    return month_name in months_with_31_days

# Test the function with the assertion
assert check_monthnumb("February") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumb("February")==False
    assert check_monthnumb("January")==True
    assert check_monthnumb("March")==True
