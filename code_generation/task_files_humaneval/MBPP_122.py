# MBPP/122
### Completion
def smartNumber(n):
    """
    Function to find the n-th smart number.
    
    A smart number is defined as a multiple of 30.
    
    Parameters:
    n (int): The position of the smart number to find (1-based index).
    
    Returns:
    int: The n-th smart number.
    """
    # Calculate the n-th smart number
    return 30 * n

# Test the function with the provided assertion
assert smartNumber(1) == 30, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert smartNumber(1) == 30
    assert smartNumber(50) == 273
    assert smartNumber(1000) == 2664
