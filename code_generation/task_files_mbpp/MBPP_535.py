# MBPP/535
### Completion
import math

def topbottom_surfacearea(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

# Test the function with the provided assertion
assert topbottom_surfacearea(10) == 314.15000000000003
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert topbottom_surfacearea(10)==314.15000000000003
    assert topbottom_surfacearea(5)==78.53750000000001
    assert topbottom_surfacearea(4)==50.264
