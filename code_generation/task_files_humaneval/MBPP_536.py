# MBPP/536
### Completion
def nth_items(lst, n):
    """
    Selects every nth item from the provided list.

    Parameters:
    lst (list): The list from which to select items.
    n (int): The step to select items.

    Returns:
    list: A list containing every nth item from the original list.
    """
    # Using list slicing to get every nth item
    return lst[::n]

# Test case
assert nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [1, 3, 5, 7, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9],2)==[1, 3, 5, 7, 9] 
    assert nth_items([10,15,19,17,16,18],3)==[10,17] 
    assert nth_items([14,16,19,15,17],4)==[14,17]
