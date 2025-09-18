# MBPP/379
### Completion
def surfacearea_cuboid(length, width, height):
    # Surface area formula for a cuboid: 2 * (length * width + width * height + height * length)
    return 2 * (length * width + width * height + height * length)

# Test the function with the provided assertion
assert surfacearea_cuboid(1, 2, 3) == 22
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cuboid(1,2,3)==22
    assert surfacearea_cuboid(5,7,9)==286
    assert surfacearea_cuboid(10,15,21)==1350
