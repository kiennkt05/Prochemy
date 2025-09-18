# MBPP/525
### Completion
def parallel_lines(line1, line2):
    """
    Check if two lines defined by two points each are parallel.
    
    Parameters:
    line1 (list): A list of two points [x1, y1, x2, y2] for the first line.
    line2 (list): A list of two points [x3, y3, x4, y4] for the second line.
    
    Returns:
    bool: True if the lines are parallel, False otherwise.
    """
    # Unpack the points for the first line
    x1, y1, x2, y2 = line1
    # Unpack the points for the second line
    x3, y3, x4, y4 = line2
    
    # Calculate the slopes
    # To avoid division by zero, we will compare the slopes using cross multiplication
    # (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3)
    # This is equivalent to:
    # (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)
    
    slope1_numerator = y2 - y1
    slope1_denominator = x2 - x1
    slope2_numerator = y4 - y3
    slope2_denominator = x4 - x3
    
    # Check if both lines are vertical
    if slope1_denominator == 0 and slope2_denominator == 0:
        return True  # Both lines are vertical and thus parallel
    
    # If one line is vertical and the other is not, they are not parallel
    if slope1_denominator == 0 or slope2_denominator == 0:
        return False
    
    # Compare slopes using cross multiplication to avoid division
    return slope1_numerator * slope2_denominator == slope2_numerator * slope1_denominator

# Test case
assert parallel_lines([2, 3, 4], [2, 3, 8]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallel_lines([2,3,4], [2,3,8]) == True
    assert parallel_lines([2,3,4], [4,-3,8]) == False
    assert parallel_lines([3,3],[5,5]) == True
