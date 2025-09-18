# MBPP/292
### Completion
def find(a, b):
    """
    This function returns the quotient of two numbers using integer division.
    
    Parameters:
    a (int): The dividend.
    b (int): The divisor.
    
    Returns:
    int: The quotient of a divided by b.
    
    Raises:
    ValueError: If b is zero, as division by zero is not allowed.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    
    return a // b  # Using integer division to get the quotient

# Test case
assert find(10, 3) == 3  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4
