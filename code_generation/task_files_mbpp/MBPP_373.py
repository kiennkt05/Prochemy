# MBPP/373
### Completion
def volume_cuboid(length, width, height):
    """Calculate the volume of a cuboid."""
    return length * width * height

# Test the function with the provided assertion
assert volume_cuboid(1, 2, 3) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cuboid(1,2,3)==6
    assert volume_cuboid(5,7,9)==315
    assert volume_cuboid(10,15,21)==3150
