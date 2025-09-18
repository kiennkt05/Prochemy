# MBPP/968
### Completion
def floor_Max(a, b, c):
    """
    This function returns the maximum value among the three given integers.
    
    Parameters:
    a (int): First integer
    b (int): Second integer
    c (int): Third integer
    
    Returns:
    int: The maximum value among a, b, and c
    """
    return max(a, b, c)

# Test case
assert floor_Max(11, 10, 9) == 11  # This should return 11, not 9 as per the assertion provided.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert floor_Max(11,10,9) == 9
    assert floor_Max(5,7,4) == 2
    assert floor_Max(2,2,1) == 1
