# MBPP/708
### Completion
def Convert(input_string):
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
assert Convert('python program') == ['python', 'program']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Convert('python program') == ['python','program']
    assert Convert('Data Analysis') ==['Data','Analysis']
    assert Convert('Hadoop Training') == ['Hadoop','Training']
