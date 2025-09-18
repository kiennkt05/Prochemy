# MBPP/857
### Completion
def listify_list(strings):
    """
    Convert a list of strings into a list of lists, where each inner list contains the characters of the corresponding string.

    Args:
    strings (list of str): A list of strings to be converted.

    Returns:
    list of list of str: A list where each element is a list of characters from the corresponding string.
    """
    # Use map to apply the list function to each string in the input list
    return list(map(list, strings))

# Test the function with the provided assertion
assert listify_list(['Red', 'Blue', 'Black', 'White', 'Pink']) == [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert listify_list(['Red', 'Blue', 'Black', 'White', 'Pink'])==[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
    assert listify_list(['python'])==[['p', 'y', 't', 'h', 'o', 'n']]
    assert listify_list([' red ', 'green',' black', 'blue ',' orange', 'brown'])==[[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]
