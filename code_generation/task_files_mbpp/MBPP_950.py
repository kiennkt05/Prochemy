# MBPP/950
### Completion
def chinese_zodiac(year):
    zodiac_signs = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 
        'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 
        'Dog', 'Pig'
    ]
    return zodiac_signs[(year - 4) % 12]

# Test the function with the provided assertion
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
