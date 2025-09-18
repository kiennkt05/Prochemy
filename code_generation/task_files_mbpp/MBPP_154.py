# MBPP/154
### Completion
def specified_element(matrix, index):
    """
    Extracts the specified element from each row of a two-dimensional list.

    Parameters:
    matrix (list of list): The two-dimensional list from which to extract elements.
    index (int): The index of the element to extract from each row.

    Returns:
    list: A list containing the specified elements from each row.
    """
    return [row[index] for row in matrix]

# Example usage
result = specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0)
assert result == [1, 4, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],3)==[2,2,5]
