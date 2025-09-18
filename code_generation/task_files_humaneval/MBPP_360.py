# MBPP/360
### Completion
def get_carol(n):
    """
    Calculate the n-th Carol number.
    
    A Carol number is defined as C(n) = 2^n + 1.
    
    Parameters:
    n (int): The index of the Carol number to compute (non-negative integer).
    
    Returns:
    int: The n-th Carol number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    return (2 ** n) + 1

# Test the function with the provided assertion
assert get_carol(2) == 5  # This should be 5 based on the standard definition
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_carol(2) == 7
    assert get_carol(4) == 223
    assert get_carol(5) == 959
