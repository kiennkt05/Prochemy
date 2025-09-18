# MBPP/76
### Completion
def count_Squares(m, n):
    """
    Count the number of squares in a rectangle of dimensions m x n.
    
    Parameters:
    m (int): The height of the rectangle.
    n (int): The width of the rectangle.
    
    Returns:
    int: The total number of squares that can fit in the rectangle.
    """
    total_squares = 0
    # Iterate over all possible square sizes
    for k in range(1, min(m, n) + 1):
        # Count the number of k x k squares
        total_squares += (m - k + 1) * (n - k + 1)
    
    return total_squares

# Test the function with the provided test case
assert count_Squares(4, 3) == 20

# Additional test cases
assert count_Squares(1, 1) == 1  # Only one 1x1 square
assert count_Squares(2, 2) == 5  # 4 (1x1) + 1 (2x2)
assert count_Squares(3, 2) == 14  # 6 (1x1) + 4 (2x2) + 1 (3x2)
assert count_Squares(5, 5) == 55  # 25 (1x1) + 16 (2x2) + 9 (3x3) + 4 (4x4) + 1 (5x5)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Squares(4,3) == 20
    assert count_Squares(2,2) == 5
    assert count_Squares(1,1) == 1
