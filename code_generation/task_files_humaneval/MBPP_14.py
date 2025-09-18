# MBPP/14
### Completion
def find_Volume(base: float, height: float, length: float) -> float:
    """
    Calculate the volume of a triangular prism.

    Parameters:
    base (float): The length of the base of the triangular face.
    height (float): The height of the triangular face.
    length (float): The length of the prism.

    Returns:
    float: The volume of the triangular prism.
    """
    # Calculate the area of the triangular base
    base_area = 0.5 * base * height
    
    # Calculate the volume of the prism
    volume = base_area * length
    
    return volume

# Test the function with the provided test case
assert find_Volume(10, 8, 6) == 240, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1
