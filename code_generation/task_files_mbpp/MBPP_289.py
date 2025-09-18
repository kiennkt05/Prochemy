# MBPP/289
### Completion
def odd_Days(year):
    # Calculate the number of days in the year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                days_in_year = 366  # Leap year
            else:
                days_in_year = 365  # Not a leap year
        else:
            days_in_year = 366  # Leap year
    else:
        days_in_year = 365  # Not a leap year

    # Calculate the number of odd days
    odd_days = days_in_year % 7
    return odd_days

# Test the function with the provided assertion
assert odd_Days(100) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Days(100) == 5
    assert odd_Days(50) ==6
    assert odd_Days(75) == 2
