# MBPP/663
### Completion
def find_max_val(x, y, limit=10**9):
    """
    Find the largest possible value of k such that k modulo x is y.
    
    Parameters:
    x (int): The divisor.
    y (int): The desired remainder.
    limit (int): The upper limit for k (default is 10^9).
    
    Returns:
    int: The largest k such that k % x == y.
    
    Raises:
    ValueError: If y is not less than x.
    """
    if y >= x:
        raise ValueError("y must be less than x.")
    
    # Calculate the largest k
    # We want k = n * x + y, where n is maximized
    # n can be calculated as (limit - y) // x
    n = (limit - y) // x
    
    # Calculate the largest k
    k = n * x + y
    
    return k

# Test case
assert find_max_val(15, 10) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_max_val(15, 10, 5) == 15
    assert find_max_val(187, 10, 5) == 185
    assert find_max_val(16, 11, 1) == 12
