# MBPP/113
### Completion
def check_integer(s: str) -> bool:
    """
    Check if the given string represents an integer.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string represents an integer, False otherwise.
    """
    # Check for negative integers
    if s.startswith('-'):
        return len(s) > 1 and s[1:].isdigit()
    
    # Check for non-negative integers
    return s.isdigit()

# Test cases
assert check_integer("python") == False  # Non-integer string
assert check_integer("123") == True       # Positive integer
assert check_integer("-123") == True      # Negative integer
assert check_integer("0") == True         # Zero as an integer
assert check_integer("12.34") == False    # Decimal number
assert check_integer("") == False          # Empty string
assert check_integer("-") == False         # Just a negative sign
assert check_integer(" 123 ") == False     # String with spaces

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True
