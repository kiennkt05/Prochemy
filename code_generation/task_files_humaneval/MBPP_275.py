# MBPP/275
### Completion
def get_Position(arr, value_to_remove, num_removals):
    """
    Find the position of the last removed element from the given array.

    Parameters:
    arr (list): The list of integers from which to remove elements.
    value_to_remove (int): The value to be removed from the array.
    num_removals (int): The number of times to remove the value.

    Returns:
    int: The index of the last removed element or -1 if not enough elements were found.
    """
    # List to store the indices of the occurrences of the value to remove
    indices = []

    # Iterate through the array to find all indices of the value to remove
    for index, value in enumerate(arr):
        if value == value_to_remove:
            indices.append(index)

    # Check if we have enough occurrences to remove
    if len(indices) < num_removals:
        return -1  # Not enough elements to remove

    # Return the index of the last occurrence that would be removed
    return indices[num_removals - 1]

# Test case
assert get_Position([2, 5, 4], 3, 2) == -1  # Not enough occurrences to remove
assert get_Position([2, 5, 4, 5, 5], 5, 2) == 3  # The second removal of 5 is at index 3
assert get_Position([1, 2, 3, 2, 2], 2, 3) == 4  # The third removal of 2 is at index 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Position([2,5,4],3,2) == 2
    assert get_Position([4,3],2,2) == 2
    assert get_Position([1,2,3,4],4,1) == 4
