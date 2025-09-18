# MBPP/808
### Completion
def check_K(tup, k):
    """
    Check if the given tuple contains the value k.

    Parameters:
    tup (tuple): The tuple to check.
    k: The value to search for in the tuple.

    Returns:
    bool: True if k is in the tuple, False otherwise.
    """
    return k in tup

# Test case
assert check_K((10, 4, 5, 6, 8), 6) == True

# Additional test cases for verification
assert check_K((10, 4, 5, 6, 8), 7) == False  # 7 is not in the tuple
assert check_K((), 6) == False               # Empty tuple, should return False
assert check_K((1, 2, 3), 1) == True         # 1 is in the tuple
assert check_K((1, 2, 3), 3) == True         # 3 is in the tuple
assert check_K((1, 2, 3), 4) == False        # 4 is not in the tuple

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_K((10, 4, 5, 6, 8), 6) == True
    assert check_K((1, 2, 3, 4, 5, 6), 7) == False
    assert check_K((7, 8, 9, 44, 11, 12), 11) == True
