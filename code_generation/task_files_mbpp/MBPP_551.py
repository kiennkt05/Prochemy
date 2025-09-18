# MBPP/551
### Completion
def extract_column(nested_list, column_index):
    return [row[column_index] for row in nested_list]

# Example usage
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
