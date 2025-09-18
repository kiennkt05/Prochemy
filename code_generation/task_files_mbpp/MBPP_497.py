# MBPP/497
### Completion
import math

def surfacearea_cone(radius, height):
    # Calculate the slant height
    slant_height = math.sqrt(radius**2 + height**2)
    # Calculate the surface area
    surface_area = math.pi * radius * (radius + slant_height)
    return surface_area

# Test the function with the provided assertion
assert surfacearea_cone(5, 12) == 282.7433388230814
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surfacearea_cone(5,12)==282.7433388230814
    assert surfacearea_cone(10,15)==880.5179353159282
    assert surfacearea_cone(19,17)==2655.923961165254
