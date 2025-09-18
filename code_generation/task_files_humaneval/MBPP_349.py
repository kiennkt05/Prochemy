# MBPP/349
### Completion
def check(s: str) -> str:
    """
    Check if the given string is a binary string.

    A binary string is defined as a string that contains only the characters '0' and '1'.

    Parameters:
    s (str): The input string to check.

    Returns:
    str: "Yes" if the string is a binary string, "No" otherwise.
    """
    # Check if all characters in the string are either '0' or '1'
    if all(char in '01' for char in s):
        return "Yes"
    else:
        return "No"

# Test case
assert check("01010101010") == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check("01010101010") == "Yes"
    assert check("name0") == "No"
    assert check("101") == "Yes"
