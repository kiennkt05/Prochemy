# MBPP/159
### Completion
def month_season(month, day):
    """
    Determine the season based on the given month and day.

    Parameters:
    month (str): The name of the month (e.g., 'January').
    day (int): The day of the month (1-31).

    Returns:
    str: The season ('winter', 'spring', 'summer', 'fall').
    """
    # Define the seasons based on month and day
    if month == 'December' and day >= 21 or month == 'January' or month == 'February' or (month == 'March' and day < 20):
        return 'winter'
    elif month == 'March' and day >= 20 or month == 'April' or month == 'May' or (month == 'June' and day < 21):
        return 'spring'
    elif month == 'June' and day >= 21 or month == 'July' or month == 'August' or (month == 'September' and day < 22):
        return 'summer'
    elif month == 'September' and day >= 22 or month == 'October' or month == 'November' or (month == 'December' and day < 21):
        return 'fall'
    else:
        return 'Invalid date'

# Test the function with the provided assertion
assert month_season('January', 4) == 'winter'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert month_season('January',4)==('winter')
    assert month_season('October',28)==('autumn')
    assert month_season('June',6)==('spring')
