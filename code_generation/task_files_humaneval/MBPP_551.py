# MBPP/551
### Completion
def extract_column(nested_list, column_index):
    """
    Extracts a specified column from a given nested list.

    Parameters:
    nested_list (list of list): A 2D list from which to extract the column.
    column_index (int): The index of the column to extract.

    Returns:
    list: A list containing the elements of the specified column.
    """
    # Using list comprehension to extract the specified column
    return [row[column_index] for row in nested_list]

# Test case
assert extract_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0) == [1, 2, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[1, 2, 1]
    assert extract_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[3, -5, 1]
    assert extract_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[1, 5, 1, 13, 5, 9]
