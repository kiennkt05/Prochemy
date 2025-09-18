# MBPP/430
### Completion
def parabola_directrix(a, h, k):
    """
    Calculate the directrix of a parabola given its parameters.
    
    Parameters:
    a (float): The coefficient that affects the width and direction of the parabola.
    h (float): The x-coordinate of the vertex of the parabola.
    k (float): The y-coordinate of the vertex of the parabola.
    
    Returns:
    float: The y-coordinate of the directrix of the parabola.
    """
    # Calculate the directrix using the formula
    directrix = k - (1 / (4 * a))
    return directrix

# Test the function with the provided assertion
assert parabola_directrix(5, 3, 2) == -198
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130
