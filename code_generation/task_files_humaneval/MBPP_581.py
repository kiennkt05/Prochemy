# MBPP/581
### Completion
import math

def surface_area(base_length, height):
    """
    Calculate the surface area of a square pyramid.

    Parameters:
    base_length (float): The length of the base of the pyramid.
    height (float): The height of the pyramid.

    Returns:
    float: The surface area of the pyramid.
    """
    # Calculate the area of the base
    base_area = base_length ** 2
    
    # Calculate the slant height using the Pythagorean theorem
    slant_height = math.sqrt((height ** 2) + (base_length / 2) ** 2)
    
    # Calculate the area of the four triangular faces
    lateral_area = 2 * base_length * slant_height
    
    # Total surface area
    total_surface_area = base_area + lateral_area
    
    return total_surface_area

# Test the function with the provided test case
assert surface_area(3, 4) == 33, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert surface_Area(3,4) == 33
    assert surface_Area(4,5) == 56
    assert surface_Area(1,2) == 5
