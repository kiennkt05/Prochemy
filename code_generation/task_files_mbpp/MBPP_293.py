# MBPP/293
### Completion
import math

def otherside_rightangle(side1, side2):
    # Calculate the hypotenuse
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return hypotenuse

# Test the function with the provided assertion
assert otherside_rightangle(7, 8) == 10.63014581273465
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert otherside_rightangle(7,8)==10.63014581273465
    assert otherside_rightangle(3,4)==5
    assert otherside_rightangle(7,15)==16.55294535724685
