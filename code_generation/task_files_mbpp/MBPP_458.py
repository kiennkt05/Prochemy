# MBPP/458
### Completion
def rectangle_area(length, width):
    return length * width

# Test the function with the provided assertion
assert rectangle_area(10, 20) == 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8
