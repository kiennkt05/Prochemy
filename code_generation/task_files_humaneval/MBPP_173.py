# MBPP/173
### Completion
import re

def remove_splchar(input_string):
    """
    Remove all non-alphanumeric characters from the input string.

    Parameters:
    input_string (str): The string from which to remove special characters.

    Returns:
    str: A string containing only alphanumeric characters.
    """
    # Use regex to substitute non-alphanumeric characters with an empty string
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    return cleaned_string

# Test case
assert remove_splchar('python  @#&^%$*program123') == 'pythonprogram123'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_splchar('python  @#&^%$*program123')==('pythonprogram123')
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')
