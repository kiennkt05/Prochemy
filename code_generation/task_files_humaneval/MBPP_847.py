# MBPP/847
### Completion
def lcopy(singleton_tuple):
    """
    Copies a list from a singleton tuple.

    Args:
    singleton_tuple (tuple): A tuple containing exactly one element, which is a list.

    Returns:
    list: A copy of the list contained in the singleton tuple.

    Raises:
    ValueError: If the input is not a singleton tuple or does not contain a list.
    """
    # Check if the input is a tuple and has exactly one element
    if not isinstance(singleton_tuple, tuple) or len(singleton_tuple) != 1:
        raise ValueError("Input must be a singleton tuple containing one element.")
    
    # Extract the list from the tuple
    extracted_list = singleton_tuple[0]
    
    # Check if the extracted element is a list
    if not isinstance(extracted_list, list):
        raise ValueError("The single element in the tuple must be a list.")
    
    # Return a copy of the list
    return extracted_list.copy()

# Test case
assert lcopy(( [1, 2, 3], )) == [1, 2, 3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert lcopy([1, 2, 3]) == [1, 2, 3]
    assert lcopy([4, 8, 2, 10, 15, 18]) == [4, 8, 2, 10, 15, 18]
    assert lcopy([4, 5, 6]) == [4, 5, 6]

