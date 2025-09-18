# MBPP/356
### Completion
def find_angle(angle1, angle2):
    # The sum of angles in a triangle is always 180 degrees
    return 180 - (angle1 + angle2)

# Test the function with the provided assertion
assert find_angle(47, 89) == 44

# You can also add some print statements to verify the output
print(find_angle(47, 89))  # Output should be 44
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_angle(47,89)==44
    assert find_angle(45,95)==40
    assert find_angle(50,40)==90
