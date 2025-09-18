# MBPP/652
### Completion
def matrix_to_list(matrix):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return '[]'  # Return an empty list representation if the matrix is empty

    # Determine the number of rows and columns
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Initialize a list to hold the tuples for each column
    column_tuples = []

    # Iterate over each column index
    for col in range(num_cols):
        # Create a tuple for the current column
        column_tuple = tuple(matrix[row][col] for row in range(num_rows))
        column_tuples.append(column_tuple)

    # Convert the list of tuples to the required string format
    return str(column_tuples)

# Test the function with the provided test case
assert matrix_to_list([[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]) == '[(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert matrix_to_list([[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]) == '[(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]'
    assert matrix_to_list([[(5, 6), (8, 9)], [(11, 14), (19, 18)], [(1, 5), (11, 2)]]) == '[(5, 8, 11, 19, 1, 11), (6, 9, 14, 18, 5, 2)]'
    assert matrix_to_list([[(6, 7), (9, 10)], [(12, 15), (20, 21)], [(23, 7), (15, 8)]]) == '[(6, 9, 12, 20, 23, 15), (7, 10, 15, 21, 7, 8)]'
