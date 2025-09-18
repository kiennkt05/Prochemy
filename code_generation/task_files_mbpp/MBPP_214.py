# MBPP/214
### Completion
import math

def degree_radian(radians):
    return radians * (180 / math.pi)

# Test the function with the provided assertion
assert degree_radian(90) == 5156.620156177409, "The conversion is incorrect."
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert degree_radian(90)==5156.620156177409
    assert degree_radian(60)==3437.746770784939
    assert degree_radian(120)==6875.493541569878
