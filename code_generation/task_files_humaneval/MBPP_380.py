# MBPP/380
### Completion
def multi_list(rows, cols):
    """
    Generate a two-dimensional array where the element at position (i, j) is equal to i * j.

    Parameters:
    rows (int): The number of rows in the array.
    cols (int): The number of columns in the array.

    Returns:
    list: A two-dimensional list (array) filled with the product of its indices.
    """
    # Initialize the two-dimensional array
    array = []
    
    # Fill the array with the product of indices
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        array.append(row)
    
    return array

# Test case
assert multi_list(3, 4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multi_list(3,4)==[[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]] 
    assert multi_list(5,7)==[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6], [0, 2, 4, 6, 8, 10, 12], [0, 3, 6, 9, 12, 15, 18], [0, 4, 8, 12, 16, 20, 24]]
    assert multi_list(10,15)==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42], [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56], [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70], [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84], [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98], [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112], [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]]
