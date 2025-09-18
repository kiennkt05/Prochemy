# MBPP/759
### Completion
import re

def is_decimal(value: str) -> bool:
    """
    Check if the input string is a decimal number with a precision of 2.
    
    Args:
    value (str): The string to check.
    
    Returns:
    bool: True if the string is a valid decimal with 2 decimal places, False otherwise.
    """
    # Regular expression to match a decimal number with up to 2 decimal places
    pattern = r'^[+-]?(\d+)(\.\d{2})?$'
    
    # Use re.match to check if the value matches the pattern
    return bool(re.match(pattern, value))

# Test cases
assert is_decimal('123.11') == True
assert is_decimal('123.1') == False  # Only one decimal place
assert is_decimal('123.111') == False  # More than two decimal places
assert is_decimal('123') == True  # No decimal point
assert is_decimal('-123.45') == True  # Negative decimal
assert is_decimal('+123.45') == True  # Positive decimal
assert is_decimal('0.00') == True  # Zero with two decimal places
assert is_decimal('0.') == False  # Zero with no decimal places
assert is_decimal('abc') == False  # Non-numeric input
assert is_decimal('123.') == False  # Decimal point without digits after

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_decimal('123.11')==True
    assert is_decimal('e666.86')==False
    assert is_decimal('3.124587')==False
