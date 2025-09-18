# MBPP/455
### Completion
def check_monthnumb_number(month):
    # List of months with 31 days
    months_with_31_days = {1, 3, 5, 7, 8, 10, 12}
    
    # Check if the month number is in the set of months with 31 days
    return month in months_with_31_days

# Test the function with the provided assertion
assert check_monthnumb_number(5) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumb_number(5)==True
    assert check_monthnumb_number(2)==False
    assert check_monthnumb_number(6)==False
