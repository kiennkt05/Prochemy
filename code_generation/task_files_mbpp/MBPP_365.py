# MBPP/365
### Completion
def count_Digit(number):
    # Convert the number to a string and count the length
    return len(str(abs(number)))

# Test the function with the provided assertion
assert count_Digit(12345) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Digit(12345) == 5
    assert count_Digit(11223305) == 8
    assert count_Digit(4123459) == 7
