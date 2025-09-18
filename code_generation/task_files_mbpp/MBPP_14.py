# MBPP/14
### Completion
def find_Volume(base, height, length):
    # Calculate the area of the triangular base
    base_area = 0.5 * base * height
    # Calculate the volume of the prism
    volume = base_area * length
    return volume

# Test the function with the provided assertion
assert find_Volume(10, 8, 6) == 240
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1
