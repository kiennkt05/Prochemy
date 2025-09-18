# MBPP/919
### Completion
def multiply_list(items):
    """
    Multiplies all items in the given list.

    Parameters:
    items (list): A list of numbers (integers or floats).

    Returns:
    int or float: The product of all numbers in the list.
    """
    product = 1  # Initialize product to 1
    for item in items:
        product *= item  # Multiply each item to the product
    return product

# Test the function with the provided test case
assert multiply_list([1, -2, 3]) == -6

# Additional test cases (optional)
assert multiply_list([2, 3, 4]) == 24
assert multiply_list([-1, -1, -1]) == -1
assert multiply_list([0, 1, 2]) == 0
assert multiply_list([]) == 1  # Multiplying an empty list should return 1

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_list([1,-2,3]) == -6
    assert multiply_list([1,2,3,4]) == 24
    assert multiply_list([3,1,2,3]) == 18
