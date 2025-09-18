# MBPP/467
### Completion
def decimal_to_octal(decimal_number):
    # Convert decimal to octal and remove the '0o' prefix
    return int(oct(decimal_number)[2:])

# Test the function with the provided assertion
assert decimal_to_octal(10) == 12

# You can also test the function with other values
print(decimal_to_octal(8))   # Output: 10
print(decimal_to_octal(15))  # Output: 17
print(decimal_to_octal(64))  # Output: 100
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decimal_to_Octal(10) == 12
    assert decimal_to_Octal(2) == 2
    assert decimal_to_Octal(33) == 41
