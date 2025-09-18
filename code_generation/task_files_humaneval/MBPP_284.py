# MBPP/284
### Completion
def check_element(lst, string):
    """
    Check if all items in the list are equal to the given string.

    Parameters:
    lst (list): The list of items to check.
    string (str): The string to compare against.

    Returns:
    bool: True if all items in the list are equal to the string, False otherwise.
    """
    # Check if all elements in the list are equal to the given string
    return all(item == string for item in lst)

# Test case
assert check_element(["green", "orange", "black", "white"], 'blue') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True
