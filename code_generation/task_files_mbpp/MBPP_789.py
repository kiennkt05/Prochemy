# MBPP/789
### Completion
def perimeter_polygon(num_sides, side_length):
    return num_sides * side_length

# Test the function with the provided assertion
assert perimeter_polygon(4, 20) == 80
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_polygon(4,20)==80
    assert perimeter_polygon(10,15)==150
    assert perimeter_polygon(9,7)==63
