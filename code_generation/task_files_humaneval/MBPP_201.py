# MBPP/201
### Completion
def chkList(lst):
    """
    Check if all elements in the list are the same.

    Parameters:
    lst (list): The list to check.

    Returns:
    bool: True if all elements are the same, False otherwise.
    """
    # If the list is empty, we consider it as having all same elements
    if not lst:
        return True
    
    # Use a set to check for unique elements
    return len(set(lst)) == 1

# Test case
assert chkList(['one', 'one', 'one']) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert chkList(['one','one','one']) == True
    assert chkList(['one','Two','Three']) == False
    assert chkList(['bigdata','python','Django']) == False
