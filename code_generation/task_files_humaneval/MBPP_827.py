# MBPP/827
### Completion
def sum_column(data, column_index):
    """
    Sums the values in a specific column of a list of lists.

    Parameters:
    data (list of lists): The input list of lists containing numerical values.
    column_index (int): The index of the column to sum.

    Returns:
    int: The sum of the specified column.
    """
    total = 0
    for row in data:
        # Check if the column index is within the bounds of the row
        if column_index < len(row):
            total += row[column_index]
    return total

# Test case
assert sum_column([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 0) == 12
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],0)==12
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],1)==15
    assert sum_column( [[1,2,3,2],[4,5,6,2],[7,8,9,5],],3)==9
