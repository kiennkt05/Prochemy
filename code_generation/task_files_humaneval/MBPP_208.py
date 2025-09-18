# MBPP/208
### Completion
import re

def is_decimal(value):
    """
    Check if the given string is a decimal number with a precision of 2.
    
    Args:
    value (str): The string to check.
    
    Returns:
    bool: True if the string is a valid decimal with up to 2 decimal places, False otherwise.
    """
    # Regex pattern to match a decimal number with up to 2 decimal places
    pattern = r'^[+-]?(\d+(\.\d{1,2})?|\.\d{1,2})$'
    
    # Use re.match to check if the value matches the pattern
    return bool(re.match(pattern, value))

# Test cases
assert is_decimal('123.11') == True
assert is_decimal('123.1') == True
assert is_decimal('123') == True
assert is_decimal('.11') == True
assert is_decimal('-.11') == True
assert is_decimal('+123.11') == True
assert is_decimal('123.111') == False  # More than 2 decimal places
assert is_decimal('123.') == False      # No digits after decimal
assert is_decimal('abc') == False       # Not a number
assert is_decimal('123.1a') == False    # Invalid characters
assert is_decimal('') == False           # Empty string

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_decimal('123.11') == True
    assert is_decimal('0.21') == True
    assert is_decimal('123.1214') == False
