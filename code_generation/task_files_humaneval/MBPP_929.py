# MBPP/929
### Completion
def count_tuplex(tup, item):
    """
    Count the occurrences of a specified item in a tuple.

    Parameters:
    tup (tuple): The tuple in which to count occurrences.
    item: The item to count in the tuple.

    Returns:
    int: The number of times the item appears in the tuple.
    """
    return tup.count(item)

# Test case
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7), 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2
    assert count_tuplex((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4
