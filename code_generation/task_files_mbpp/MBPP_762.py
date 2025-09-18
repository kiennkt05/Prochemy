# MBPP/762
### Completion
def check_monthnumber_number(month):
    # Months with 30 days: April (4), June (6), September (9), November (11)
    return month in [4, 6, 9, 11]

# Test the function with the provided assertion
assert check_monthnumber_number(6) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_monthnumber_number(6)==True
    assert check_monthnumber_number(2)==False
    assert check_monthnumber_number(12)==False
