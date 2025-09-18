# MBPP/736
### Completion
def left_insertion(sorted_list, value):
    """
    Find the left insertion point for a specified value in a sorted list.

    Parameters:
    sorted_list (list): A list of sorted elements.
    value: The value to insert.

    Returns:
    int: The index at which the value can be inserted to maintain sorted order.
    """
    low, high = 0, len(sorted_list)
    
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < value:
            low = mid + 1
        else:
            high = mid
    
    return low

# Test case
assert left_insertion([1, 2, 4, 5], 6) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,4,5],3)==2
    assert left_insertion([1,2,4,5],7)==4
