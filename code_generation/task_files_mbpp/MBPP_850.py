# MBPP/850
### Completion
def is_triangleexists(angle1, angle2, angle3):
    # Check if all angles are positive and their sum is 180
    return angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180

# Test the function with the provided assertion
assert is_triangleexists(50, 60, 70) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_triangleexists(50,60,70)==True
    assert is_triangleexists(90,45,45)==True
    assert is_triangleexists(150,30,70)==False
