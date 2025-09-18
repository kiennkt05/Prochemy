# MBPP/190
### Completion
def count_integral_points(x1, y1, x2, y2):
    """
    Count the number of integral coordinates that lie strictly inside a square
    defined by its bottom-left corner (x1, y1) and top-right corner (x2, y2).

    Parameters:
    x1 (int): x-coordinate of the bottom-left corner
    y1 (int): y-coordinate of the bottom-left corner
    x2 (int): x-coordinate of the top-right corner
    y2 (int): y-coordinate of the top-right corner

    Returns:
    int: Number of integral coordinates inside the square
    """
    # Calculate the number of integral points along the x-axis
    x_count = max(0, x2 - x1 - 1)
    # Calculate the number of integral points along the y-axis
    y_count = max(0, y2 - y1 - 1)
    
    # Total integral points inside the square
    return x_count * y_count

# Test case
assert count_integral_points(1, 1, 4, 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Intgral_Points(1,1,4,4) == 4
    assert count_Intgral_Points(1,2,1,2) == 1
    assert count_Intgral_Points(4,2,6,4) == 1
