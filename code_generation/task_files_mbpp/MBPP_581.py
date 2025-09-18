# MBPP/581
### Completion
import math

def surface_Area(side, height):
    # Calculate the base area
    base_area = side ** 2
    
    # Calculate the slant height
    slant_height = math.sqrt(height ** 2 + (side / 2) ** 2)
    
    # Calculate the lateral area
    lateral_area = (4 * side * slant_height) / 2
    
    # Total surface area
    total_surface_area = base_area + lateral_area
    
    return total_surface_area

# Test the function with the provided assertion
assert surface_Area(3, 4) == 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5
