# MBPP/205
### Completion
def inversion_elements(input_tuple):
    """
    This function takes a tuple of integers and returns a new tuple
    where each element is the negative of the original element minus 1.
    
    Parameters:
    input_tuple (tuple): A tuple of integers.
    
    Returns:
    tuple: A new tuple with inverted elements.
    """
    # Create a new tuple with inverted elements
    inverted_tuple = tuple(-element - 1 for element in input_tuple)
    return inverted_tuple

# Test the function with the provided test case
assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)

# If the assertion passes, the function works as expected.
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert inversion_elements((7, 8, 9, 1, 10, 7)) == (-8, -9, -10, -2, -11, -8)
    assert inversion_elements((2, 4, 5, 6, 1, 7)) == (-3, -5, -6, -7, -2, -8)
    assert inversion_elements((8, 9, 11, 14, 12, 13)) == (-9, -10, -12, -15, -13, -14)
