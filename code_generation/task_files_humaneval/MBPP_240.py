# MBPP/240
### Completion
def replace_list(original, new):
    """
    Replace the last element of the original list with the elements of the new list.

    Parameters:
    original (list): The original list from which the last element will be replaced.
    new (list): The new list that will replace the last element of the original list.

    Returns:
    list: The modified original list with the last element replaced by the new list.
    """
    # Check if the original list is not empty
    if original:
        # Remove the last element
        original.pop()
    # Extend the original list with the new list
    original.extend(new)
    return original

# Test case
assert replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]
