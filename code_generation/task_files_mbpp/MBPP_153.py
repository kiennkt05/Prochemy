# MBPP/153
### Completion
def parabola_vertex(a, b, c):
    # Calculate the x-coordinate of the vertex
    x_vertex = -b / (2 * a)
    # Calculate the y-coordinate of the vertex
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    return (x_vertex, y_vertex)

# Test the function with the provided assertion
assert parabola_vertex(5, 3, 2) == (-0.3, 1.55)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parabola_vertex(5,3,2)==(-0.3, 1.55)
    assert parabola_vertex(9,8,4)==(-0.4444444444444444, 2.2222222222222223)
    assert parabola_vertex(2,4,6)==(-1.0, 4.0)
