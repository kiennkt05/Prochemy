# MBPP/353
### Completion
def remove_column(nested_list, col_index):
    """
    Remove a specified column from a given nested list.

    Parameters:
    nested_list (list of list): The input nested list from which to remove the column.
    col_index (int): The index of the column to be removed.

    Returns:
    list of list: A new nested list with the specified column removed.
    """
    # Create a new nested list with the specified column removed
    return [[item for idx, item in enumerate(sublist) if idx != col_index] for sublist in nested_list]

# Test case
assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0) == [[2, 3], [4, 5], [1, 1]]

# Additional test cases for verification
assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1) == [[1, 3], [2, 5], [1, 1]]
assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 2) == [[1, 2], [2, 4], [1, 1]]
assert remove_column([[1, 2], [3, 4]], 0) == [[2], [4]]
assert remove_column([[1], [2], [3]], 0) == [[], [], []]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[[2, 3], [4, 5], [1, 1]]
    assert remove_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[[1, 2], [-2, 4], [1, -1]]
    assert remove_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[[3], [7], [3], [15, 17], [7], [11]]
