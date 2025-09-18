# MBPP/726
### Completion
def multiply_elements(input_tuple):
    """
    Multiplies adjacent elements of the given tuple.

    Args:
    input_tuple (tuple): A tuple of numbers.

    Returns:
    tuple: A tuple containing the products of adjacent elements.
    """
    # Initialize an empty list to store the results
    result = []
    
    # Loop through the tuple, multiplying adjacent elements
    for i in range(len(input_tuple) - 1):
        product = input_tuple[i] * input_tuple[i + 1]
        result.append(product)
    
    # Convert the result list back to a tuple
    return tuple(result)

# Test the function with the provided test case
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)

# Additional test cases can be added to verify the function
print(multiply_elements((1, 2, 3)))  # Expected output: (2, 6)
print(multiply_elements((4, 5, 6)))  # Expected output: (20, 30)
print(multiply_elements((0, 1, 2)))  # Expected output: (0, 2)
print(multiply_elements((10,)))       # Expected output: () since there's only one element
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
