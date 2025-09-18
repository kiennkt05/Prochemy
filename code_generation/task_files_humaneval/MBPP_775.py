# MBPP/775
### Completion
def odd_position(lst):
    """
    Check if every element at odd indices in the list is an odd number.

    Parameters:
    lst (list): The list of numbers to check.

    Returns:
    bool: True if all elements at odd indices are odd, False otherwise.
    """
    # Iterate through the list using the index
    for index in range(1, len(lst), 2):  # Start from index 1 and step by 2
        if lst[index] % 2 == 0:  # Check if the number is even
            return False  # If any number at an odd index is even, return False
    return True  # If all checks passed, return True

# Test case
assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_position([2,1,4,3,6,7,6,3]) == True
    assert odd_position([4,1,2]) == True
    assert odd_position([1,2,3]) == False
