# MBPP/198
### Completion
def largest_triangle(a, b):
    # Calculate the area of the largest triangle inscribed in the ellipse
    area = 2 * a * b
    return area

# Test the function with the provided assertion
assert largest_triangle(4, 2) == 10.392304845413264
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert largest_triangle(4,2)==10.392304845413264
    assert largest_triangle(5,7)==4.639421805988064
    assert largest_triangle(9,1)==105.2220865598093
