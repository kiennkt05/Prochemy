# MBPP/95
### Completion
def Find_Min_Length(lists):
    """
    Find the minimum length of sublists in a list of lists.

    Parameters:
    lists (list of list): A list containing sublists.

    Returns:
    int: The minimum length of the sublists.
    """
    # Check if the input list is empty
    if not lists:
        return 0  # Return 0 if there are no sublists

    # Initialize min_length with the length of the first sublist
    min_length = len(lists[0])

    # Iterate through each sublist to find the minimum length
    for sublist in lists:
        current_length = len(sublist)
        if current_length < min_length:
            min_length = current_length

    return min_length

# Test case
assert Find_Min_Length([[1], [1, 2]]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
