# MBPP/730
### Completion
def consecutive_duplicates(input_list):
    """
    Remove consecutive duplicates from the given list.

    Parameters:
    input_list (list): The list from which to remove consecutive duplicates.

    Returns:
    list: A new list with consecutive duplicates removed.
    """
    if not input_list:  # Check if the input list is empty
        return []

    result = [input_list[0]]  # Start with the first element

    for current in input_list[1:]:  # Iterate through the list starting from the second element
        if current != result[-1]:  # Compare with the last element in the result
            result.append(current)  # Append if it's different

    return result

# Test case
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[10, 15, 19, 18, 17, 26, 17, 18, 10]
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']
