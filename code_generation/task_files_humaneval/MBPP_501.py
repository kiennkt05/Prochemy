# MBPP/501
### Completion
def num_comm_div(a, b):
    """
    Function to find the greatest common divisor (GCD) of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return abs(a)  # Return the absolute value of GCD

# Test case
assert num_comm_div(2, 4) == 2  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert num_comm_div(2,4) == 2
    assert num_comm_div(2,8) == 2
    assert num_comm_div(12,24) == 6
