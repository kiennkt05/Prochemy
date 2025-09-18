# MBPP/600
### Completion
def is_Even(num):
    """
    Check if the given number is even using a bitwise operator.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return (num & 1) == 0

# Test cases
assert is_Even(1) == False  # 1 is odd
assert is_Even(2) == True   # 2 is even
assert is_Even(0) == True   # 0 is even
assert is_Even(-2) == True  # -2 is even
assert is_Even(-3) == False # -3 is odd

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False
