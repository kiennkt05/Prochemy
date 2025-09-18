# MBPP/624
### Completion
def is_upper(input_string):
    """
    Convert the given string to upper case.

    Parameters:
    input_string (str): The string to be converted to upper case.

    Returns:
    str: The upper case version of the input string.
    """
    return input_string.upper()

# Test case
assert is_upper("person") == "PERSON", "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_upper("person") =="PERSON"
    assert is_upper("final") == "FINAL"
    assert is_upper("Valid") == "VALID"
