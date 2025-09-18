# MBPP/740
### Completion
def tuple_to_dict(tup):
    """
    Convert a given tuple to a dictionary using adjacent elements as key-value pairs.
    
    Args:
    tup (tuple): A tuple containing elements to be converted into a dictionary.
    
    Returns:
    dict: A dictionary with keys and values from the tuple.
    
    Raises:
    ValueError: If the tuple has an odd number of elements.
    """
    # Check if the length of the tuple is even
    if len(tup) % 2 != 0:
        raise ValueError("The tuple must have an even number of elements.")
    
    # Create a dictionary from the tuple
    result_dict = {}
    for i in range(0, len(tup), 2):
        key = tup[i]
        value = tup[i + 1]
        result_dict[key] = value
    
    return result_dict

# Test case
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
