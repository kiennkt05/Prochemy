# MBPP/353
### Completion
def remove_column(nested_list, col_index):
    # Use a list comprehension to create a new nested list without the specified column
    return [[row[i] for i in range(len(row)) if i != col_index] for row in nested_list]

# Test the function with the provided assertion
assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0) == [[2, 3], [4, 5], [1, 1]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]],0)==[[2, 3], [4, 5], [1, 1]]
    assert remove_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],2)==[[1, 2], [-2, 4], [1, -1]]
    assert remove_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]],0)==[[3], [7], [3], [15, 17], [7], [11]]
