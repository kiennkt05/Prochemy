# MBPP/835
### Completion
def slope(x1, y1, x2, y2):
    """
    Calculate the slope of a line given two points (x1, y1) and (x2, y2).
    
    Parameters:
    x1 (float): x-coordinate of the first point
    y1 (float): y-coordinate of the first point
    x2 (float): x-coordinate of the second point
    y2 (float): y-coordinate of the second point
    
    Returns:
    float: The slope of the line connecting the two points.
           Returns None if the slope is undefined (vertical line).
    """
    if x1 == x2:
        return None  # Slope is undefined for vertical lines
    return (y2 - y1) / (x2 - x1)

# Test case
assert slope(4, 2, 2, 5) == -1.5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert slope(4,2,2,5) == -1.5
    assert slope(2,4,4,6) == 1
    assert slope(1,2,4,2) == 0
