# MBPP/35
### Completion
def find_rect_num(n):
    """
    Calculate the n-th rectangular number.
    
    A rectangular number is defined as the product of two consecutive integers:
    R(n) = n * (n + 1)
    
    Parameters:
    n (int): The index of the rectangular number to find.
    
    Returns:
    int: The n-th rectangular number.
    """
    # Calculate the n-th rectangular number
    return n * (n + 1)

# Test case
assert find_rect_num(4) == 20, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_rect_num(4) == 20
    assert find_rect_num(5) == 30
    assert find_rect_num(6) == 42
