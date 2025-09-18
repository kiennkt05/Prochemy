# MBPP/226
### Completion
def odd_values_string(s: str) -> str:
    """
    Remove characters from the string that have odd index values.

    Parameters:
    s (str): The input string from which to remove characters.

    Returns:
    str: A new string with characters at odd indices removed.
    """
    # Use list comprehension to select characters at even indices
    result = ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
    return result

# Test case
assert odd_values_string('abcdef') == 'ace'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
