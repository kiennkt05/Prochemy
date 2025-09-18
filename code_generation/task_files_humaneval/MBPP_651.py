# MBPP/651
### Completion
def check_subset(superset, subset):
    """
    Check if the 'subset' tuple is a subset of the 'superset' tuple.

    Parameters:
    superset (tuple): The tuple to check against.
    subset (tuple): The tuple to check if it is a subset.

    Returns:
    bool: True if 'subset' is a subset of 'superset', False otherwise.
    """
    # Convert the superset tuple to a set for efficient lookup
    superset_set = set(superset)
    
    # Check if all elements in subset are in the superset set
    for element in subset:
        if element not in superset_set:
            return False
    return True

# Test case
assert check_subset((10, 4, 5, 6), (5, 10)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset((10, 4, 5, 6), (5, 10)) == True
    assert check_subset((1, 2, 3, 4), (5, 6)) == False
    assert check_subset((7, 8, 9, 10), (10, 8)) == True
