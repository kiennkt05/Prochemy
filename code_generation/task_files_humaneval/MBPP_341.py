# MBPP/341
### Completion
def set_to_tuple(input_set):
    """
    Convert a given set into an ordered tuple.

    Parameters:
    input_set (set): A set of elements to be converted.

    Returns:
    tuple: A tuple containing the elements of the set in sorted order.
    """
    # Convert the set to a sorted list
    sorted_list = sorted(input_set)
    # Convert the sorted list to a tuple
    result_tuple = tuple(sorted_list)
    return result_tuple

# Test case
assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
    assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
    assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)
