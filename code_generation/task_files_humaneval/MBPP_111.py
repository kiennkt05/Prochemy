# MBPP/111
### Completion
def common_in_nested_lists(nested_lists):
    """
    Find common elements in a list of nested lists.

    Parameters:
    nested_lists (list of list): A list containing multiple lists of integers.

    Returns:
    list: A list of common elements found in all nested lists.
    """
    if not nested_lists:
        return []

    # Start with the first list converted to a set
    common_elements = set(nested_lists[0])

    # Iterate through the remaining lists and update the common elements
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)

    # Convert the result back to a sorted list
    return sorted(common_elements)

# Test case
assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == [12, 18]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])==[18, 12]
    assert common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])==[5,23]
    assert common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]])==[4]
