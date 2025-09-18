# MBPP/58
### Completion
def opposite_Signs(a: int, b: int) -> bool:
    """
    Check if two integers have opposite signs.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    bool: True if the integers have opposite signs, False otherwise.
    """
    return (a < 0) != (b < 0)

# Test case
assert opposite_Signs(1, -2) == True

# Additional test cases for verification
assert opposite_Signs(-1, 2) == True
assert opposite_Signs(0, -2) == False
assert opposite_Signs(2, 0) == False
assert opposite_Signs(-3, -5) == False
assert opposite_Signs(3, 5) == False

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert opposite_Signs(1,-2) == True
    assert opposite_Signs(3,2) == False
    assert opposite_Signs(-10,-10) == False
