# MBPP/176
### Completion
def perimeter_triangle(a, b, c):
    """Calculate the perimeter of a triangle given its three sides."""
    return a + b + c

# Test the function with the provided assertion
assert perimeter_triangle(10, 20, 30) == 60
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_triangle(10,20,30)==60
    assert perimeter_triangle(3,4,5)==12
    assert perimeter_triangle(25,35,45)==105
