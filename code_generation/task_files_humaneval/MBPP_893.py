# MBPP/893
### Completion
def Extract(sublists):
    """
    Extracts the last element from each sublist.

    Parameters:
    sublists (list of list): A list containing sublists from which to extract the last elements.

    Returns:
    list: A list containing the last element of each sublist.
    """
    # Using list comprehension to get the last element of each sublist
    return [sublist[-1] for sublist in sublists if sublist]  # Check if sublist is not empty

# Test case
assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]

# Additional test cases
assert Extract([[1], [2, 3], [4, 5, 6]]) == [1, 3, 6]
assert Extract([[], [1, 2], [3]]) == [2, 3]  # Should handle empty sublists
assert Extract([[], [], []]) == []  # All empty sublists should return an empty list
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
    assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']
    assert Extract([[1, 2, 3], [4, 5]]) == [3, 5]
