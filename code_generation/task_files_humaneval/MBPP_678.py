# MBPP/678
### Completion
def remove_spaces(input_string: str) -> str:
    """
    Remove all spaces from the given string.

    Parameters:
    input_string (str): The string from which spaces will be removed.

    Returns:
    str: The input string without any spaces.
    """
    # Replace all spaces with an empty string
    return input_string.replace(" ", "")

# Test case
assert remove_spaces("a b c") == "abc"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_spaces("a b c") == "abc"
    assert remove_spaces("1 2 3") == "123"
    assert remove_spaces(" b c") == "bc"
