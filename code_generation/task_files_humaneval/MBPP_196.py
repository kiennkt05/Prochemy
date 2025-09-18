# MBPP/196
### Completion
def remove_tuples(tuples_list, k):
    """
    Remove all tuples from the list that have a length of k.

    Parameters:
    tuples_list (list of tuples): The list of tuples to filter.
    k (int): The length of tuples to remove.

    Returns:
    list of tuples: A new list with tuples of length k removed.
    """
    # Using list comprehension to filter out tuples of length k
    return [t for t in tuples_list if len(t) != k]

# Test case
assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]

# Additional test cases can be added to further validate the function
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuples([(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] , 1) == [(4, 5), (8, 6, 7), (3, 4, 6, 7)]
    assert remove_tuples([(4, 5), (4,5), (6, 7), (1, 2, 3), (3, 4, 6, 7)] ,2) == [(1, 2, 3), (3, 4, 6, 7)]
    assert remove_tuples([(1, 4, 4), (4, 3), (8, 6, 7), (1, ), (3, 6, 7)] , 3) == [(4, 3), (1,)]
