# MBPP/587
### Completion
def list_tuple(input_list):
    """
    Convert a list to a tuple.

    Parameters:
    input_list (list): The list to be converted.

    Returns:
    tuple: A tuple containing the elements of the input list.
    """
    return tuple(input_list)

# Test case
assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)

# If the assertion passes, the function works as expected.
print("Function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
    assert list_tuple([2, 4, 5, 6, 2, 3, 4, 4, 7])==(2, 4, 5, 6, 2, 3, 4, 4, 7)
    assert list_tuple([58,44,56])==(58,44,56)
