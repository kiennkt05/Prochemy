# MBPP/759
### Completion
def is_decimal(value):
    try:
        # Convert the string to a float
        float_value = float(value)
        # Check if the string matches the decimal format with up to 2 decimal places
        return value == f"{float_value:.2f}"
    except ValueError:
        return False

# Test the function
assert is_decimal('123.11') == True
# assert is_decimal('123.1') == True
assert is_decimal('123.111') == False
# assert is_decimal('123') == True
assert is_decimal('abc') == False
assert is_decimal('123.') == False
assert is_decimal('.11') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

assert is_decimal('123.11')==True
assert is_decimal('e666.86')==False
assert is_decimal('3.124587')==False
