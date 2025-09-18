# MBPP/435
### Completion
def last_Digit(number):
    return abs(number) % 10

# Test the function
assert last_Digit(123) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0
