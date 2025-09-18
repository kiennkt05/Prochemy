# MBPP/278
### Completion
def count_first_elements(tup):
    """
    Count the number of elements that occur before the last element (record) in the given tuple.

    Parameters:
    tup (tuple): The input tuple from which to count elements.

    Returns:
    int: The count of elements before the last element in the tuple.
    """
    # Check if the tuple is empty
    if not tup:
        return 0
    
    # The last element (record) in the tuple
    record = tup[-1]
    
    # Count the number of elements before the last element
    count = len(tup) - 1  # Subtracting 1 to exclude the last element itself
    
    return count

# Test case
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 4  # There are 4 elements before 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
    assert count_first_elements((2, 9, (5, 7), 11) ) == 2
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4
