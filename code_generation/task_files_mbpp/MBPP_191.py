# MBPP/191
### Completion
def check_monthnumber(month_name):
    # List of months that have 30 days
    months_with_30_days = ["April", "June", "September", "November"]
    
    # Check if the given month is in the list of months with 30 days
    return month_name in months_with_30_days

# Test the function with the provided assertion
assert check_monthnumber("February") == False

# You can also test other months
print(check_monthnumber("April"))   # True
print(check_monthnumber("January"))  # False
print(check_monthnumber("June"))     # True
print(check_monthnumber("December"))  # False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumber("February")==False
    assert check_monthnumber("June")==True
    assert check_monthnumber("April")==True
