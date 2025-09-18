# MBPP/920
### Completion
def remove_tuple(tuple_list):
    """
    Remove all tuples that contain only None values from the given list of tuples.

    Args:
    tuple_list (list of tuples): A list containing tuples.

    Returns:
    str: A string representation of the filtered list of tuples.
    """
    # Filter out tuples that contain only None values
    filtered_tuples = [tup for tup in tuple_list if any(value is not None for value in tup)]
    
    # Return the filtered list as a string
    return str(filtered_tuples)

# Test case
assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )]) == '[(None, 2), (3, 4), (12, 3)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'
    assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'
    assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'
