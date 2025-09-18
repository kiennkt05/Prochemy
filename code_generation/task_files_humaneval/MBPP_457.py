# MBPP/457
### Completion
def Find_Min(lists):
    """
    Find the sublist with the minimum length from a list of lists.

    Parameters:
    lists (list of list): A list containing sublists.

    Returns:
    list: The sublist with the minimum length.
    """
    if not lists:
        return []  # Return an empty list if the input is empty

    # Initialize the minimum length and the corresponding sublist
    min_length = float('inf')
    min_sublist = []

    # Iterate through each sublist
    for sublist in lists:
        # Check if the current sublist is shorter than the minimum found so far
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist

    return min_sublist

# Test case
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
