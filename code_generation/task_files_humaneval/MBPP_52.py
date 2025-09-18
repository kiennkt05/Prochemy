# MBPP/52
### Completion
def parallelogram_area(base, height):
    """
    Calculate the area of a parallelogram.

    Parameters:
    base (float): The length of the base of the parallelogram.
    height (float): The height of the parallelogram.

    Returns:
    float: The area of the parallelogram.
    """
    return base * height

# Test case
assert parallelogram_area(10, 20) == 200, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parallelogram_area(10,20)==200
    assert parallelogram_area(15,20)==300
    assert parallelogram_area(8,9)==72
