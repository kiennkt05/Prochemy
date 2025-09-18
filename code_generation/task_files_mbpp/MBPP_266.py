# MBPP/266
### Completion
def lateralsurface_cube(side):
    return 4 * (side ** 2)

# Test the function with the provided assertion
assert lateralsurface_cube(5) == 100
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400
