# MBPP/553
### Completion
def tuple_to_float(tup):
    """
    Convert a tuple of two integers into a floating-point number.
    
    The first element of the tuple represents the integer part,
    and the second element represents the fractional part.
    
    Args:
    tup (tuple): A tuple containing two integers (integer_part, fractional_part).
    
    Returns:
    float: The combined floating-point number.
    """
    if len(tup) != 2:
        raise ValueError("Input tuple must contain exactly two elements.")
    
    integer_part = tup[0]
    fractional_part = tup[1]
    
    # Calculate the number of digits in the fractional part
    fractional_length = len(str(fractional_part))
    
    # Combine the integer and fractional parts
    result = integer_part + fractional_part / (10 ** fractional_length)
    
    return result

# Test case
assert tuple_to_float((4, 56)) == 4.56
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_float((4, 56)) == 4.56
    assert tuple_to_float((7, 256)) == 7.256
    assert tuple_to_float((8, 123)) == 8.123
