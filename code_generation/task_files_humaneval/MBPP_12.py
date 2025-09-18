# MBPP/12
### Completion
def sort_matrix(matrix):
    """
    Sorts a given matrix in ascending order according to the sum of its rows.

    Parameters:
    matrix (list of list of int): The matrix to be sorted.

    Returns:
    list of list of int: The sorted matrix.
    """
    # Sort the matrix using the sum of each row as the key
    sorted_matrix = sorted(matrix, key=sum)
    return sorted_matrix

# Test case
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]
