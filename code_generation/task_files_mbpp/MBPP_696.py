# MBPP/696
### Completion
def zip_list(list1, list2):
    # Use zip to combine the two lists and then flatten the result
    return [sublist1 + sublist2 for sublist1, sublist2 in zip(list1, list2)]

# Test the function with the provided assertion
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
