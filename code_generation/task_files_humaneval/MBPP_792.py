# MBPP/792
### Completion
def count_list(lists):
    """
    Count the number of lists in a given list of lists.

    Parameters:
    lists (list): A list containing multiple lists.

    Returns:
    int: The number of lists contained in the input list.
    """
    return len(lists)

# Test case
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert count_list([[1,2],[2,3],[4,5]]) == 3
    assert count_list([[1,0],[2,0]]) == 2
