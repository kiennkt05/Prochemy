# MBPP/827
### Completion
def sum_column(matrix, column_index):
    """
    Sums the values in a specific column of a list of lists.

    :param matrix: List of lists containing numerical values
    :param column_index: Index of the column to sum
    :return: Sum of the specified column
    """
    return sum(row[column_index] for row in matrix)

# Example usage and assertion
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
