# MBPP/208
### Completion
import re

def is_decimal(value):
    # Regular expression to match a decimal number with up to 2 decimal places
    pattern = r'^\d+(\.\d{1,2})?$'
    return bool(re.match(pattern, value))

# Test the function
assert is_decimal('123.11') == True
assert is_decimal('123.1') == True
assert is_decimal('123') == True
assert is_decimal('123.111') == False
assert is_decimal('abc') == False
assert is_decimal('123.') == False
assert is_decimal('.11') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_decimal('123.11') == True
    assert is_decimal('0.21') == True
    assert is_decimal('123.1214') == False
