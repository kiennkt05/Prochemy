# MBPP/869
### Completion
def remove_list_range(lists, lower, upper):
    """
    Remove sublists from the given list of lists that contain elements outside the specified range.

    Parameters:
    lists (list of list of int): The list of lists to filter.
    lower (int): The lower bound of the range (inclusive).
    upper (int): The upper bound of the range (inclusive).

    Returns:
    list of list of int: A new list containing only the sublists with all elements within the specified range.
    """
    result = []
    for sublist in lists:
        # Check if all elements in the sublist are within the specified range
        if all(lower <= item <= upper for item in sublist):
            result.append(sublist)
    return result

# Test case
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17) == [[13, 14, 15, 17]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]
    assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]
