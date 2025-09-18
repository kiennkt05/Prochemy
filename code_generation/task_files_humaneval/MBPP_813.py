# MBPP/813
### Completion
def string_length(s: str) -> int:
    """
    Returns the length of the given string.

    Parameters:
    s (str): The string whose length is to be calculated.

    Returns:
    int: The length of the string.
    """
    return len(s)

# Test case
assert string_length('python') == 6, "Test case failed: Expected length of 'python' to be 6"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_length('python')==6
    assert string_length('program')==7
    assert string_length('language')==8
