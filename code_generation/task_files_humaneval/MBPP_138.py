# MBPP/138
### Completion
def is_Sum_Of_Powers_Of_Two(n):
    """
    Check if the given number can be represented as a sum of non-zero powers of 2.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number can be represented as a sum of non-zero powers of 2, False otherwise.
    """
    # A number can be represented as a sum of non-zero powers of 2 if it is greater than 0
    return n > 0

# Test case
assert is_Sum_Of_Powers_Of_Two(10) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True
