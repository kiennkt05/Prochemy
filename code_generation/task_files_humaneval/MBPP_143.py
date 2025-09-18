# MBPP/143
### Completion
def find_lists(input_tuple):
    """
    This function counts the number of lists present in the given tuple.

    Parameters:
    input_tuple (tuple): A tuple containing various elements.

    Returns:
    int: The count of lists in the tuple.
    """
    count = 0  # Initialize count of lists
    for element in input_tuple:
        if isinstance(element, list):  # Check if the element is a list
            count += 1  # Increment count if it is a list
    return count  # Return the total count of lists

# Test case
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
    assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
