# MBPP/118
### Completion
def string_to_list(input_string):
    """
    Convert a string to a list of words.

    Parameters:
    input_string (str): The string to be converted.

    Returns:
    list: A list of words extracted from the input string.
    """
    # Split the input string into a list of words
    return input_string.split()

# Test case
assert string_to_list("python programming") == ['python', 'programming']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_to_list("python programming")==['python','programming']
    assert string_to_list("lists tuples strings")==['lists','tuples','strings']
    assert string_to_list("write a program")==['write','a','program']
