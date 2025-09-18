# MBPP/786
### Completion
def right_insertion(sorted_list, value):
    """
    Locate the right insertion point for a specified value in sorted order.

    Parameters:
    sorted_list (list): A list of sorted elements.
    value: The value to be inserted.

    Returns:
    int: The index at which the value should be inserted.
    """
    low, high = 0, len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] <= value:
            low = mid + 1
        else:
            high = mid

    return low

# Example usage
assert right_insertion([1, 2, 4, 5], 6) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert right_insertion([1,2,4,5],6)==4
    assert right_insertion([1,2,4,5],3)==2
    assert right_insertion([1,2,4,5],7)==4
