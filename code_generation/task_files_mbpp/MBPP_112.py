# MBPP/112
### Completion
import math

def perimeter(radius, height):
    # Calculate the circumference of the base
    circumference = 2 * math.pi * radius
    # The perimeter is the circumference plus the height
    return circumference + height

# Test the function with the provided assertion
assert perimeter(2, 4) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter(2,4) == 12
    assert perimeter(1,2) == 6
    assert perimeter(3,1) == 8
