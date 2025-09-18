# MBPP/892
### Completion
def remove_spaces(input_string):
    """
    Remove multiple spaces from the input string and return a string with single spaces between words.

    Parameters:
    input_string (str): The string from which to remove extra spaces.

    Returns:
    str: A string with multiple spaces removed.
    """
    # Split the string into words and join them with a single space
    return ' '.join(input_string.split())

# Test case
assert remove_spaces('python  program') == 'python program'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_spaces('python  program')==('python program')
    assert remove_spaces('python   programming    language')==('python programming language')
    assert remove_spaces('python                     program')==('python program')
