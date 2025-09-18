# MBPP/913
### Completion
def end_num(s: str) -> bool:
    """
    Check if the given string ends with a number.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string ends with a number, False otherwise.
    """
    # Check if the string is not empty and the last character is a digit
    if s and s[-1].isdigit():
        return True
    return False

# Test case
assert end_num('abcdef') == False  # The string 'abcdef' does not end with a number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert end_num('abcdef')==False
    assert end_num('abcdef7')==True
    assert end_num('abc')==False
