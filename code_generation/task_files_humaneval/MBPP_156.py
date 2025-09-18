# MBPP/156
### Completion
def tuple_int_str(input_tuple):
    """
    Convert a tuple of string values to a tuple of integer values.

    Args:
    input_tuple (tuple): A tuple containing tuples of string values.

    Returns:
    tuple: A tuple containing tuples of integer values.
    """
    # Use a nested tuple comprehension to convert strings to integers
    return tuple(tuple(int(value) for value in inner) for inner in input_tuple)

# Test case
assert tuple_int_str((('333', '33'), ('1416', '55'))) == ((333, 33), (1416, 55))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_int_str((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))
    assert tuple_int_str((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))
    assert tuple_int_str((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))
