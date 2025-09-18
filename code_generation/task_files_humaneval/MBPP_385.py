# MBPP/385
### Completion
def get_perrin(n):
    """
    Calculate the n-th Perrin number using recursion.

    Parameters:
    n (int): The index of the Perrin number to compute.

    Returns:
    int: The n-th Perrin number.
    """
    # Base cases
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Recursive case
        return get_perrin(n - 2) + get_perrin(n - 3)

# Test case
assert get_perrin(9) == 12

# Additional test cases for verification
assert get_perrin(0) == 3
assert get_perrin(1) == 0
assert get_perrin(2) == 2
assert get_perrin(3) == 3
assert get_perrin(4) == 2
assert get_perrin(5) == 5
assert get_perrin(6) == 5
assert get_perrin(7) == 8
assert get_perrin(8) == 10

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_perrin(9) == 12
    assert get_perrin(4) == 2
    assert get_perrin(6) == 5
