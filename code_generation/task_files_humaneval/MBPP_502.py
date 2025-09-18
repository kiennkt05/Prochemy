# MBPP/502
### Completion
def find(a, b):
    """
    This function returns the remainder of the division of a by b.
    
    Parameters:
    a (int): The dividend.
    b (int): The divisor.
    
    Returns:
    int: The remainder of a divided by b.
    """
    return a % b

# Test case
assert find(3, 3) == 0  # This should pass as 3 % 3 is 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find(3,3) == 0
    assert find(10,3) == 1
    assert find(16,5) == 1
