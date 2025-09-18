# MBPP/318
### Completion
def max_volume(S):
    # Calculate the side length when the sum of sides is S
    side_length = S / 12
    # Calculate the volume
    volume = side_length ** 3
    return volume

# Test the function with the provided assertion
assert max_volume(8) == 18
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_volume(8) == 18
    assert max_volume(4) == 2
    assert max_volume(1) == 0
