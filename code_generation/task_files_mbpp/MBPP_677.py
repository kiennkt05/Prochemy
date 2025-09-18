# MBPP/677
### Completion
def validity_triangle(angle1, angle2, angle3):
    # Check if the sum of the angles is 180 and each angle is greater than 0
    return angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180

# Test the function with the provided assertion
assert validity_triangle(60, 50, 90) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert validity_triangle(60,50,90)==False
    assert validity_triangle(45,75,60)==True
    assert validity_triangle(30,50,100)==True
