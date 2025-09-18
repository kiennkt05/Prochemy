# MBPP/761
### Completion
import math

def arc_length(radius, angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    # Calculate arc length
    return radius * angle_radians

# Test the function with the provided assertion
assert arc_length(9, 45) == 3.5357142857142856
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert arc_length(9,45)==3.5357142857142856
    assert arc_length(9,480)==None
    assert arc_length(5,270)==11.785714285714285
