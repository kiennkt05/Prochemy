# MBPP/941
### Completion
def count_elim(lst):
    """
    Counts the number of elements in the list until a tuple is encountered.

    Parameters:
    lst (list): The list to count elements from.

    Returns:
    int: The count of elements before the first tuple.
    """
    count = 0  # Initialize the counter
    for element in lst:
        if isinstance(element, tuple):  # Check if the element is a tuple
            break  # Stop counting if a tuple is found
        count += 1  # Increment the counter for non-tuple elements
    return count  # Return the final count

# Test case
assert count_elim([10, 20, 30, (10, 20), 40]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_elim([10,20,30,(10,20),40])==3
    assert count_elim([10,(20,30),(10,20),40])==1
    assert count_elim([(10,(20,30,(10,20),40))])==0
