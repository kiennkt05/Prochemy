# MBPP/421
### Completion
def concatenate_tuple(elements, delimiter='-'):
    """
    Concatenates each element of the tuple into a single string using the specified delimiter.

    Parameters:
    elements (tuple): A tuple containing elements to concatenate.
    delimiter (str): The delimiter to use for concatenation (default is '-').

    Returns:
    str: A single string with all elements concatenated by the delimiter.
    """
    # Convert each element to string and join them with the delimiter
    return delimiter.join(str(element) for element in elements)

# Test case
assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'
