# MBPP/347
### Completion
def count_Squares(m, n):
    """
    Count the number of squares in a rectangle of dimensions m x n.

    Parameters:
    m (int): The height of the rectangle.
    n (int): The width of the rectangle.

    Returns:
    int: The total number of squares in the rectangle.
    """
    total_squares = 0
    # Iterate over all possible square sizes
    for k in range(1, min(m, n) + 1):
        # Count how many k x k squares can fit in the m x n rectangle
        total_squares += (m - k + 1) * (n - k + 1)
    
    return total_squares

# Test the function with the provided test case
assert count_Squares(4, 3) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Squares(4,3) == 20
    assert count_Squares(1,2) == 2
    assert count_Squares(2,2) == 5
