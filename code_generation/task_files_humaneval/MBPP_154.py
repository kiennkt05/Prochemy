# MBPP/154
### Completion
def specified_element(two_d_list, index):
    """
    Extracts the specified element from each sublist in a two-dimensional list.

    Parameters:
    two_d_list (list of list): The two-dimensional list from which to extract elements.
    index (int): The index of the element to extract from each sublist.

    Returns:
    list: A list containing the extracted elements.
    """
    # Using list comprehension to extract the specified element from each sublist
    return [sublist[index] for sublist in two_d_list]

# Test case
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0) == [1, 4, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],3)==[2,2,5]
