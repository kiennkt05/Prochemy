# MBPP/328
### Completion
def rotate_left(lst, num_rotations, start_index):
    """
    Rotate the list to the left by a specified number of items starting from a given index.

    Parameters:
    lst (list): The list to be rotated.
    num_rotations (int): The number of positions to rotate the list to the left.
    start_index (int): The index from which to start the rotation.

    Returns:
    list: The rotated list.
    """
    # Ensure the start_index is within the bounds of the list
    if start_index < 0 or start_index >= len(lst):
        raise ValueError("start_index must be within the bounds of the list")

    # Calculate the effective number of rotations
    effective_rotations = num_rotations % len(lst)

    # Slice the list into two parts and concatenate them
    rotated_part = lst[start_index + effective_rotations:] + lst[start_index:start_index + effective_rotations]
    # Add the elements before the start_index
    rotated_list = lst[:start_index] + rotated_part

    return rotated_list

# Test case
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4) == [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2]
