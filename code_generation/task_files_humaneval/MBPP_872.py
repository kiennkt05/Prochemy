# MBPP/872
### Completion
def check_subset(nested_list1, nested_list2):
    """
    Check if nested_list1 is a subset of nested_list2.

    Parameters:
    nested_list1 (list of list): The first nested list to check.
    nested_list2 (list of list): The second nested list to check against.

    Returns:
    bool: True if nested_list1 is a subset of nested_list2, False otherwise.
    """
    # Convert nested_list2 to a set of tuples for easier comparison
    set_nested_list2 = {tuple(sublist) for sublist in nested_list2}
    
    # Check if each sublist in nested_list1 is in the set of nested_list2
    for sublist in nested_list1:
        if tuple(sublist) not in set_nested_list2:
            return False
            
    return True

# Test case
assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
    assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
    assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False
