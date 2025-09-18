# MBPP/234
### Completion
def volume_cube(side_length):
    """Calculate the volume of a cube given the length of its side."""
    return side_length ** 3

# Test the function
assert volume_cube(3) == 27
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125
