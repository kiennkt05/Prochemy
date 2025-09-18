# MBPP/626
### Completion
def triangle_area(radius):
    if radius <= 0:
        return 0
    return radius ** 2

# Test the function with the provided assertion
assert triangle_area(0) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert triangle_area(0) == 0
    assert triangle_area(-1) == -1
    assert triangle_area(2) == 4
