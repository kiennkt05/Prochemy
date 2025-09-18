# MBPP/945
### Completion
def tuple_to_set(input_tuple):
    """
    Convert a given tuple into a set.

    Parameters:
    input_tuple (tuple): The tuple to be converted.

    Returns:
    set: A set containing the elements of the input tuple.
    """
    return set(input_tuple)

# Test case
assert tuple_to_set(('x', 'y', 'z')) == {'y', 'x', 'z'}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_set(('x', 'y', 'z') ) == {'y', 'x', 'z'}
    assert tuple_to_set(('a', 'b', 'c') ) == {'c', 'a', 'b'}
    assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}
