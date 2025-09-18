# MBPP/394
### Completion
def check_distinct(tup):
    """
    Check if all elements in the given tuple are distinct.

    Parameters:
    tup (tuple): The tuple to check for distinct elements.

    Returns:
    bool: True if all elements are distinct, False otherwise.
    """
    # Convert the tuple to a set to remove duplicates
    distinct_elements = set(tup)
    
    # Compare the length of the set with the length of the tuple
    return len(distinct_elements) == len(tup)

# Test case
assert check_distinct((1, 4, 5, 6, 1, 4)) == False  # There are duplicates
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True
