# MBPP/431
### Completion
def common_element(list1, list2):
    """
    Check if there is at least one common element between two lists.

    Parameters:
    list1 (list): The first list of elements.
    list2 (list): The second list of elements.

    Returns:
    bool: True if there is at least one common element, False otherwise.
    """
    # Convert the first list to a set for O(1) average time complexity on lookups
    set1 = set(list1)
    
    # Iterate through the second list and check for common elements
    for element in list2:
        if element in set1:
            return True  # Found a common element
    
    return False  # No common elements found

# Test case
assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
    assert common_element([1,2,3,4,5], [6,7,8,9])==None
    assert common_element(['a','b','c'], ['d','b','e'])==True
