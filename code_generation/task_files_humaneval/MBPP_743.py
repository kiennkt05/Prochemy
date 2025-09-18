# MBPP/743
### Completion
def rotate_right(lst, num_items, length):
    """
    Rotate the list `lst` to the right by `num_items` positions.
    
    Parameters:
    lst (list): The list to be rotated.
    num_items (int): The number of positions to rotate the list.
    length (int): The length of the list (for validation).
    
    Returns:
    list: The rotated list.
    """
    # Ensure the number of items to rotate is within the bounds of the list length
    num_items = num_items % length
    
    # Perform the rotation
    return lst[-num_items:] + lst[:-num_items]

# Test case
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 10) == [8, 9, 10, 1, 2, 3, 4, 5, 6]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[8, 9, 10, 1, 2, 3, 4, 5, 6]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
