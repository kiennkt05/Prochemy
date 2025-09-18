# MBPP/69
### Completion
def is_sublist(main_list, sub_list):
    """
    Check if sub_list is a sublist of main_list.

    Parameters:
    main_list (list): The list in which to search for the sublist.
    sub_list (list): The list to search for in the main list.

    Returns:
    bool: True if sub_list is found in main_list, False otherwise.
    """
    # Get the lengths of the main list and the sublist
    len_main = len(main_list)
    len_sub = len(sub_list)

    # If the sublist is longer than the main list, it cannot be a sublist
    if len_sub > len_main:
        return False

    # Iterate through the main list
    for i in range(len_main - len_sub + 1):
        # Check if the sublist matches the slice of the main list
        if main_list[i:i + len_sub] == sub_list:
            return True

    return False

# Test case
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_sublist([2,4,3,5,7],[3,7])==False
    assert is_sublist([2,4,3,5,7],[4,3])==True
    assert is_sublist([2,4,3,5,7],[1,6])==False
