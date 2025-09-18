# MBPP/533
### Completion
def remove_datatype(input_tuple, data_type):
    """
    Remove elements of a specified data type from the given tuple.

    Parameters:
    input_tuple (tuple): The tuple from which to remove elements.
    data_type (type): The data type to remove from the tuple.

    Returns:
    list: A list of elements from the tuple that are not of the specified data type.
    """
    # Using list comprehension to filter out elements of the specified data type
    return [element for element in input_tuple if not isinstance(element, data_type)]

# Test case
assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]

# Additional test cases for verification
assert remove_datatype((1, 2, 3, 'a', 'b', 4.5), str) == [1, 2, 3, 4.5]
assert remove_datatype((True, False, 0, 1, 2), bool) == [0, 1, 2]
assert remove_datatype((None, 1, 2, 3), type(None)) == [1, 2, 3]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
    assert remove_datatype((7, 8, 9, "SR"), str) == [7, 8, 9]
    assert remove_datatype((7, 1.1, 2, 2.2), float) == [7, 2]
