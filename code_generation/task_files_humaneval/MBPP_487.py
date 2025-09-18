# MBPP/487
### Completion
def sort_tuple(tuples_list):
    """
    Sorts a list of tuples in increasing order by the last element in each tuple.

    Parameters:
    tuples_list (list of tuples): The list of tuples to be sorted.

    Returns:
    list of tuples: The sorted list of tuples.
    """
    # Sort the list of tuples using the last element of each tuple as the key
    return sorted(tuples_list, key=lambda x: x[-1])

# Test case
assert sort_tuple([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_tuple([(1, 3), (3, 2), (2, 1)] ) == [(2, 1), (3, 2), (1, 3)]
    assert sort_tuple([(2, 4), (3, 3), (1, 1)] ) == [(1, 1), (3, 3), (2, 4)]
    assert sort_tuple([(3, 9), (6, 7), (4, 3)] ) == [(4, 3), (6, 7), (3, 9)]
