# MBPP/460
### Completion
def Extract(sublists):
    """
    Extract the first element from each sublist.

    Parameters:
    sublists (list of list): A list containing sublists.

    Returns:
    list: A list containing the first element of each sublist.
    """
    # Using list comprehension to get the first element of each sublist
    return [sublist[0] for sublist in sublists if sublist]  # Check if sublist is not empty

# Test case
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]

# Additional test cases
assert Extract([[10, 20], [30], [40, 50, 60]]) == [10, 30, 40]
assert Extract([[], [1, 2], [3]]) == [1, 3]  # Handles empty sublist
assert Extract([]) == []  # Handles empty input
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert Extract([[1,2,3],[4, 5]]) == [1,4]
    assert Extract([[9,8,1],[1,2]]) == [9,1]
