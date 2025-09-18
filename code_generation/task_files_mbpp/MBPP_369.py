# MBPP/369
### Completion
def lateralsurface_cuboid(length, width, height):
    return 2 * height * (length + width)

# Test the function with the provided assertion
assert lateralsurface_cuboid(8, 5, 6) == 156
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cuboid(8,5,6)==156
    assert lateralsurface_cuboid(7,9,10)==320
    assert lateralsurface_cuboid(10,20,30)==1800
