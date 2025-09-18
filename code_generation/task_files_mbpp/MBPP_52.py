# MBPP/52
### Completion
def parallelogram_area(base, height):
    """Calculate the area of a parallelogram given its base and height."""
    return base * height

# Test the function with the provided assertion
assert parallelogram_area(10, 20) == 200
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallelogram_area(10,20)==200
    assert parallelogram_area(15,20)==300
    assert parallelogram_area(8,9)==72
