# MBPP/894
### Completion
def float_to_tuple(float_string):
    """
    Convert a string of float values separated by commas into a tuple of floats.

    Parameters:
    float_string (str): A string containing float values separated by commas.

    Returns:
    tuple: A tuple containing the float values.
    """
    # Split the string by commas and strip any whitespace
    float_list = float_string.split(',')
    
    # Convert each element to float and create a tuple
    float_tuple = tuple(float(value.strip()) for value in float_list)
    
    return float_tuple

# Test case
assert float_to_tuple("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)

# Additional test cases for verification
assert float_to_tuple("0.1, 0.2") == (0.1, 0.2)
assert float_to_tuple("3.14, 2.71, 1.41") == (3.14, 2.71, 1.41)
assert float_to_tuple("  5.0 ,  6.0  ") == (5.0, 6.0)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert float_to_tuple("1.2, 1.3, 2.3, 2.4, 6.5") == (1.2, 1.3, 2.3, 2.4, 6.5)
    assert float_to_tuple("2.3, 2.4, 5.6, 5.4, 8.9") == (2.3, 2.4, 5.6, 5.4, 8.9)
    assert float_to_tuple("0.3, 0.5, 7.8, 9.4") == (0.3, 0.5, 7.8, 9.4)
