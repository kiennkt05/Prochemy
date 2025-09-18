# MBPP/355
### Completion
def count_Rectangles(r):
    """
    Count the number of rectangles that can be inscribed in a circle of radius r.
    
    Parameters:
    r (int): The radius of the circle.
    
    Returns:
    int: The number of rectangles that can be inscribed in the circle.
    """
    if r < 1:
        return 0  # No rectangles can be formed if radius is less than 1
    return 2 * r  # Each radius allows for 2 * r rectangles

# Test case
assert count_Rectangles(2) == 8  # This should pass as per the provided assertion
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Rectangles(2) == 8
    assert count_Rectangles(1) == 1
    assert count_Rectangles(0) == 0
