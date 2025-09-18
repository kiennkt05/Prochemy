# MBPP/441
### Completion
def surfacearea_cube(side_length):
    """Calculate the surface area of a cube given the length of its side."""
    return 6 * (side_length ** 2)

# Test the function with the provided assertion
assert surfacearea_cube(5) == 150
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600
