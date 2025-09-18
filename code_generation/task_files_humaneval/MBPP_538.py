# MBPP/538
### Completion
def string_list_to_tuple(input_string):
    """
    Convert a given string to a tuple of its characters.

    Parameters:
    input_string (str): The string to be converted.

    Returns:
    tuple: A tuple containing each character of the input string.
    """
    return tuple(input_string)

# Test case
assert string_list_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_list_to_tuple(("python 3.0")) == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_list_to_tuple(("bigdata")) == ('b', 'i', 'g', 'd', 'a', 't', 'a')
    assert string_list_to_tuple(("language")) == ('l', 'a', 'n', 'g', 'u', 'a', 'g','e')
