# MBPP/479
### Completion
def first_Digit(number):
    # Convert the number to a string and get the first character
    first_digit = str(abs(number))[0]
    return int(first_digit)

# Test the function with the provided assertion
assert first_Digit(123) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1
