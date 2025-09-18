# MBPP/494
### Completion
def binary_to_integer(binary_tuple):
    """
    Convert a binary tuple to an integer and return it as a string.
    
    Parameters:
    binary_tuple (tuple): A tuple containing binary digits (0s and 1s).
    
    Returns:
    str: The integer value of the binary tuple as a string.
    """
    # Convert the tuple to a string
    binary_string = ''.join(str(bit) for bit in binary_tuple)
    
    # Convert the binary string to an integer
    integer_value = int(binary_string, 2)
    
    # Return the integer value as a string
    return str(integer_value)

# Test the function with the provided test case
assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
    assert binary_to_integer((0, 1, 1, 0, 0, 1, 0, 1)) == '101'
    assert binary_to_integer((1, 1, 0, 1, 0, 1)) == '53'
