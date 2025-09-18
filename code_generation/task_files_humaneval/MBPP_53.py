# MBPP/53
### Completion
def check_Equality(s: str) -> str:
    """
    Check if the first and last characters of the given string are equal.

    Parameters:
    s (str): The input string to check.

    Returns:
    str: "Equal" if the first and last characters are the same, "Not Equal" otherwise.
    """
    # Check if the string is empty
    if len(s) == 0:
        return "The string is empty"
    
    # Compare the first and last characters
    if s[0] == s[-1]:
        return "Equal"
    else:
        return "Not Equal"

# Test case
assert check_Equality("abcda") == "Equal"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Equality("abcda") == "Equal"
    assert check_Equality("ab") == "Not Equal"
    assert check_Equality("mad") == "Not Equal"
