# MBPP/525
### Completion
def parallel_lines(line1, line2):
    # Unpack the points from the input lists
    x1, y1, x2, y2 = line1[0], line1[1], line1[2], line1[3]
    x3, y3, x4, y4 = line2[0], line2[1], line2[2], line2[3]
    
    # Calculate the slopes of both lines
    # To avoid division by zero, we will compare the cross products instead
    slope1_numerator = y2 - y1
    slope1_denominator = x2 - x1
    slope2_numerator = y4 - y3
    slope2_denominator = x4 - x3
    
    # Check if the slopes are equal using cross multiplication
    return slope1_numerator * slope2_denominator == slope2_numerator * slope1_denominator

# Example usage
assert parallel_lines([2, 3, 4, 5], [2, 3, 8, 9]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallel_lines([2,3,4], [2,3,8]) == True
    assert parallel_lines([2,3,4], [4,-3,8]) == False
    assert parallel_lines([3,3],[5,5]) == True
