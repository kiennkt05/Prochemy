# MBPP/896
### Completion
def sort_list_last(tuples_list):
    """
    Sorts a list of non-empty tuples in increasing order by the last element of each tuple.

    Parameters:
    tuples_list (list of tuples): A list containing non-empty tuples.

    Returns:
    list of tuples: A new list sorted by the last element of each tuple.
    """
    # Sort the list using the last element of each tuple as the key
    return sorted(tuples_list, key=lambda x: x[-1])

# Test case
assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]) == [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# If you want to see the output of the function, you can uncomment the following line:
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])==[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 
    assert sort_list_last([(9,8), (4, 7), (3,5), (7,9), (1,2)])==[(1,2), (3,5), (4,7), (9,8), (7,9)] 
    assert sort_list_last([(20,50), (10,20), (40,40)])==[(10,20),(40,40),(20,50)] 
