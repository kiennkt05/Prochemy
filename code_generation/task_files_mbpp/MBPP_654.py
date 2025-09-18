# MBPP/654
### Completion
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Test the function with the provided assertion
assert rectangle_perimeter(10, 20) == 60
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rectangle_perimeter(10,20)==60
    assert rectangle_perimeter(10,5)==30
    assert rectangle_perimeter(4,2)==12
