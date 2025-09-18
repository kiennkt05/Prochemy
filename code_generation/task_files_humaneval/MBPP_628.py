# MBPP/628
### Completion
def replace_spaces(input_string):
    """
    Replace all spaces in the given string with '%20'.

    Parameters:
    input_string (str): The string in which spaces will be replaced.

    Returns:
    str: The modified string with spaces replaced by '%20'.
    """
    # Replace spaces with '%20'
    return input_string.replace(' ', '%20')

# Test case
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'

# You can add more test cases to validate the function further
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    assert replace_spaces("I am a Programmer") == 'I%20am%20a%20Programmer'
    assert replace_spaces("I love Coding") == 'I%20love%20Coding'
