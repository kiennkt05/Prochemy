# MBPP/950
### Completion
def chinese_zodiac(year):
    """
    Determine the Chinese zodiac sign for a given year.

    Parameters:
    year (int): The year for which to determine the zodiac sign.

    Returns:
    str: The Chinese zodiac sign corresponding to the given year.
    """
    # List of zodiac signs in order
    zodiac_signs = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 
        'Snake', 'Horse', 'Goat', 'Monkey', 
        'Rooster', 'Dog', 'Pig'
    ]
    
    # The base year for the zodiac cycle
    base_year = 1924
    
    # Calculate the index in the zodiac_signs list
    index = (year - base_year) % 12
    
    # Return the corresponding zodiac sign
    return zodiac_signs[index]

# Test case
assert chinese_zodiac(1997) == 'Ox'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert chinese_zodiac(1997)==('Ox')
    assert chinese_zodiac(1998)==('Tiger')
    assert chinese_zodiac(1994)==('Dog')
