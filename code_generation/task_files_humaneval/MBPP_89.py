# MBPP/89
### Completion
def closest_num(n):
    """
    Returns the closest smaller number than n.
    
    Parameters:
    n (int): The number to find the closest smaller number for.
    
    Returns:
    int: The closest smaller number than n.
    """
    return n - 1

# Test case
assert closest_num(11) == 10  # This should pass without any assertion error
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11
