# MBPP/513
### Completion
def add_str(tup, string):
    """
    Convert a tuple into a list by adding the given string after every element.

    Parameters:
    tup (tuple): The input tuple containing elements.
    string (str): The string to be added after each element.

    Returns:
    list: A list containing elements from the tuple followed by the string.
    """
    result = []
    for element in tup:
        result.append(element)  # Add the element from the tuple
        result.append(string)    # Add the specified string
    return result

# Test case
assert add_str((5, 6, 7, 4, 9), "FDF") == [5, 'FDF', 6, 'FDF', 7, 'FDF', 4, 'FDF', 9, 'FDF']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_str((5, 6, 7, 4, 9) , "FDF") == [5, 'FDF', 6, 'FDF', 7, 'FDF', 4, 'FDF', 9, 'FDF']
    assert add_str((7, 8, 9, 10) , "PF") == [7, 'PF', 8, 'PF', 9, 'PF', 10, 'PF']
    assert add_str((11, 14, 12, 1, 4) , "JH") == [11, 'JH', 14, 'JH', 12, 'JH', 1, 'JH', 4, 'JH']
