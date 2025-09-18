# MBPP/696
### Completion
def zip_list(list1, list2):
    """
    Zips two lists of lists by concatenating corresponding sublists.

    Parameters:
    list1 (list of list): The first list of lists.
    list2 (list of list): The second list of lists.

    Returns:
    list of list: A new list of lists where each sublist is the concatenation
                  of the corresponding sublists from list1 and list2.
    """
    # Use list comprehension to zip the two lists of lists
    return [sublist1 + sublist2 for sublist1, sublist2 in zip(list1, list2)]

# Test case
assert zip_list([[1, 3], [5, 7], [9, 11]], [[2, 4], [6, 8], [10, 12, 14]]) == [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert zip_list([[1, 3], [5, 7], [9, 11]] ,[[2, 4], [6, 8], [10, 12, 14]] )==[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
    assert zip_list([[1, 2], [3, 4], [5, 6]] ,[[7, 8], [9, 10], [11, 12]] )==[[1, 2, 7, 8], [3, 4, 9, 10], [5, 6, 11, 12]]
    assert zip_list([['a','b'],['c','d']] , [['e','f'],['g','h']] )==[['a','b','e','f'],['c','d','g','h']]
