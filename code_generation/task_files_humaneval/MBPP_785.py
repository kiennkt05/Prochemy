# MBPP/785
### Completion
def tuple_str_int(tuple_str):
    """
    Convert a tuple string to an integer tuple.

    Parameters:
    tuple_str (str): A string representation of a tuple, e.g., "(7, 8, 9)"

    Returns:
    tuple: A tuple of integers, e.g., (7, 8, 9)
    """
    # Remove the parentheses and split the string by commas
    # Strip whitespace to ensure clean conversion
    elements = tuple_str.strip("()").split(",")
    
    # Convert each element to an integer and return as a tuple
    return tuple(int(element.strip()) for element in elements)

# Test case
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# Additional test cases for verification
assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
assert tuple_str_int("(10, 20, 30)") == (10, 20, 30)
assert tuple_str_int("(0, -1, 5)") == (0, -1, 5)
assert tuple_str_int("(100, 200)") == (100, 200)

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
