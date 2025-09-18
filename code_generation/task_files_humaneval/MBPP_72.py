# MBPP/72
### Completion
def dif_Square(n):
    """
    Check if the given number can be represented as the difference of two squares.

    A number n can be expressed as the difference of two squares if it is not of the form 4k + 2.
    
    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n can be expressed as the difference of two squares, False otherwise.
    """
    # Check if n is of the form 4k + 2
    if n % 4 == 2:
        return False
    return True

# Test case
assert dif_Square(5) == True  # 5 can be expressed as 3^2 - 2^2 (9 - 4)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True
