# MBPP/565
### Completion
def split(s: str) -> list:
    """
    Splits a string into a list of its characters.

    Parameters:
    s (str): The string to be split.

    Returns:
    list: A list containing the characters of the string.
    """
    return list(s)

# Test case
assert split('python') == ['p', 'y', 't', 'h', 'o', 'n'], "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']
