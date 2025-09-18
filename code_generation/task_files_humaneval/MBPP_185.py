# MBPP/185
### Completion
def parabola_focus(a, b, c):
    """
    Calculate the focus of a parabola given its coefficients a, b, and c.
    
    The parabola is in the form y = ax^2 + bx + c.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    tuple: A tuple containing the coordinates of the focus (x_f, y_f)
    """
    # Calculate the x-coordinate of the focus
    x_f = -b / (2 * a)
    
    # Calculate the distance p from the vertex to the focus
    p = 1 / (4 * a)
    
    # Calculate the y-coordinate of the focus
    y_f = (a * x_f**2 + b * x_f + c) + p
    
    return (x_f, y_f)

# Test the function with the provided assertion
assert parabola_focus(5, 3, 2) == (-0.3, 1.6)

# If you want to see the output for the test case
print(parabola_focus(5, 3, 2))  # Output should be (-0.3, 1.6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parabola_focus(5,3,2)==(-0.3, 1.6)
    assert parabola_focus(9,8,4)==(-0.4444444444444444, 2.25)
    assert parabola_focus(2,4,6)==(-1.0, 4.125)
