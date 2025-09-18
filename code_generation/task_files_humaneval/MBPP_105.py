# MBPP/105
### Completion
def count(boolean_list):
    """
    Count the number of True boolean values in the given list.

    Parameters:
    boolean_list (list): A list containing boolean values (True or False).

    Returns:
    int: The count of True values in the list.
    """
    return sum(1 for value in boolean_list if value is True)

# Test case
assert count([True, False, True]) == 2

# Additional test cases for verification
assert count([True, True, True]) == 3
assert count([False, False, False]) == 0
assert count([]) == 0
assert count([True, False, True, False, True]) == 3

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3
