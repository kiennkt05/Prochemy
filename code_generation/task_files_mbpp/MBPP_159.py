# MBPP/159
### Completion
def month_season(month, day):
    month = month.lower()
    
    if month == 'december':
        return 'winter' if day >= 21 else 'fall'
    elif month == 'january' or month == 'february':
        return 'winter'
    elif month == 'march':
        return 'winter' if day < 20 else 'spring'
    elif month == 'april' or month == 'may':
        return 'spring'
    elif month == 'june':
        return 'spring' if day < 21 else 'summer'
    elif month == 'july' or month == 'august':
        return 'summer'
    elif month == 'september':
        return 'summer' if day < 22 else 'fall'
    elif month == 'october' or month == 'november':
        return 'fall'
    else:
        return 'Invalid month'

# Example usage
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
