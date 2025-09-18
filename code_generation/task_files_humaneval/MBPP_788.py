# MBPP/788
### Completion
def new_tuple(lst, string):
    """
    Create a new tuple from the given list and string.

    Parameters:
    lst (list): A list of elements to be included in the tuple.
    string (str): A string to be included in the tuple.

    Returns:
    tuple: A new tuple containing elements from the list and the string.
    """
    # Convert the list to a tuple
    tuple_from_list = tuple(lst)
    
    # Create a new tuple by combining the tuple from the list and the string
    result_tuple = tuple_from_list + (string,)
    
    return result_tuple

# Test case
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
