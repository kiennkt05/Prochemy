# MBPP/467
### Completion
def decimal_to_octal(decimal_number):
    """
    Convert a decimal number to its octal representation.

    Parameters:
    decimal_number (int): The decimal number to convert.

    Returns:
    str: The octal representation of the decimal number.
    """
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if decimal_number == 0:
        return "0"
    
    octal_digits = []
    
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_digits.append(str(remainder))
        decimal_number //= 8
    
    # The digits are in reverse order, so we need to reverse them
    octal_digits.reverse()
    
    # Join the list into a string and return
    return ''.join(octal_digits)

# Test case
assert decimal_to_octal(10) == '12'  # The octal representation of 10 is 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decimal_to_Octal(10) == 12
    assert decimal_to_Octal(2) == 2
    assert decimal_to_Octal(33) == 41
