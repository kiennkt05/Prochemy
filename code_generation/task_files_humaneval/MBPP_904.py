# MBPP/904
### Completion
def even_num(n):
    """
    Check if the given number is even.

    Parameters:
    n (int, float): The number to check.

    Returns:
    bool: True if n is an even integer, False otherwise.
    """
    # Check if n is an integer and if it is even
    if isinstance(n, int) and n % 2 == 0:
        return True
    return False

# Test case
assert even_num(13.5) == False  # This should pass as 13.5 is not an even integer
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_num(13.5)==False
    assert even_num(0)==True
    assert even_num(-9)==False
