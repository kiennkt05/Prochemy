# MBPP/161
### Completion
def remove_elements(original_list, elements_to_remove):
    """
    Remove all elements from original_list that are present in elements_to_remove.

    Parameters:
    original_list (list): The list from which elements will be removed.
    elements_to_remove (list): The list of elements to remove from original_list.

    Returns:
    list: A new list with the elements removed.
    """
    # Create a new list with elements not in elements_to_remove
    result = [item for item in original_list if item not in elements_to_remove]
    return result

# Test case
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_elements([1,2,3,4,5,6,7,8,9,10],[2,4,6,8])==[1, 3, 5, 7, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7])==[2, 4, 6, 8, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7])==[1, 2, 3, 4, 6, 8, 9, 10]
