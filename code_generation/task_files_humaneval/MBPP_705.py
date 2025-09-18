# MBPP/705
### Completion
def sort_sublists(lst):
    """
    Sorts a list of lists first by the length of the sublists,
    and then by the values within the sublists.

    Parameters:
    lst (list of list): A list containing sublists to be sorted.

    Returns:
    list of list: A new list containing the sorted sublists.
    """
    # Sort by length of sublist and then by the sublist values
    return sorted(lst, key=lambda x: (len(x), x))

# Test case
assert sort_sublists([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]) == [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_sublists([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]])==[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
    assert sort_sublists([[1], [2, 3], [4, 5, 6], [7], [10, 11]])==[[1], [7], [2, 3], [10, 11], [4, 5, 6]]
    assert sort_sublists([["python"],["java","C","C++"],["DBMS"],["SQL","HTML"]])==[['DBMS'], ['python'], ['SQL', 'HTML'], ['java', 'C', 'C++']]
