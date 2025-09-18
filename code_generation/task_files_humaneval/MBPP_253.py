# MBPP/253
### Completion
def count_integer(lst):
    """
    Count the number of integers in a given list.

    Parameters:
    lst (list): The list to count integers from.

    Returns:
    int: The count of integers in the list.
    """
    count = 0  # Initialize the counter
    for item in lst:  # Iterate through each item in the list
        if isinstance(item, int):  # Check if the item is an integer
            count += 1  # Increment the counter if it is an integer
    return count  # Return the final count

# Test case
assert count_integer([1, 2, 'abc', 1.2]) == 2  # This should pass
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_integer([1,2,'abc',1.2]) == 2
    assert count_integer([1,2,3]) == 3
    assert count_integer([1,1.2,4,5.1]) == 2
