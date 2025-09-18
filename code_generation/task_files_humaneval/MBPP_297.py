# MBPP/297
### Completion
def flatten_list(nested_list):
    """
    Flattens a given nested list structure.

    Args:
    nested_list (list): A list that may contain nested lists.

    Returns:
    list: A flattened list containing all the elements from the nested structure.
    """
    flattened = []
    
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, extend the flattened list with the flattened sublist
            flattened.extend(flatten_list(element))
        else:
            # If the element is not a list, append it to the flattened list
            flattened.append(element)
    
    return flattened

# Test case
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    assert flatten_list([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[10, 20, 40, 30, 56, 25, 10, 20, 33, 40]
    assert flatten_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[1, 2, 3, 4, 5, 6, 10, 11, 12, 7, 8, 9]
