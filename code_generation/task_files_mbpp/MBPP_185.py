# MBPP/185
### Completion
def parabola_focus(a, b, c):
    # Calculate the vertex (h, k)
    h = -b / (2 * a)
    k = a * (h ** 2) + b * h + c
    
    # Calculate p
    p = 1 / (4 * a)
    
    # Focus coordinates
    focus_x = h
    focus_y = k + p
    
    return (focus_x, focus_y)

# Test the function with the provided assertion
assert parabola_focus(5, 3, 2) == (-0.3, 1.6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parabola_focus(5,3,2)==(-0.3, 1.6)
    assert parabola_focus(9,8,4)==(-0.4444444444444444, 2.25)
    assert parabola_focus(2,4,6)==(-1.0, 4.125)
