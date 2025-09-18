# MBPP/202
### Completion
def remove_even(s: str) -> str:
    """
    Remove characters at even indices from the input string.

    Parameters:
    s (str): The input string from which to remove even-indexed characters.

    Returns:
    str: A new string with characters at even indices removed.
    """
    # Using a list comprehension to collect characters at odd indices
    result = ''.join(s[i] for i in range(len(s)) if i % 2 != 0)
    return result

# Test case
assert remove_even("python") == "pto"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_even("python")==("pto")
    assert remove_even("program")==("porm")
    assert remove_even("language")==("lnug")
