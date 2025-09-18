# MBPP/801
### Completion
def test_three_equal(a: int, b: int, c: int) -> int:
    """
    Count the number of equal integers among three given integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.

    Returns:
    int: The count of equal integers (0, 1, 2, or 3).
    """
    # Initialize a count variable
    count = 0
    
    # Check for equality among the three integers
    if a == b and b == c:
        count = 3  # All three are equal
    elif a == b or b == c or a == c:
        count = 2  # Two are equal
    else:
        count = 0  # No numbers are equal
    
    return count

# Test case
assert test_three_equal(1, 1, 1) == 3  # All three numbers are equal
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_three_equal(1,1,1) == 3
    assert test_three_equal(-1,-2,-3) == 0
    assert test_three_equal(1,2,2) == 2
