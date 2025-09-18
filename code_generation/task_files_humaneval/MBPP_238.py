# MBPP/238
### Completion
def number_of_substrings(s: str) -> int:
    """
    Count the number of non-empty substrings of the given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of non-empty substrings.
    """
    n = len(s)  # Get the length of the string
    # Calculate the number of non-empty substrings using the formula
    return n * (n + 1) // 2

# Test case
assert number_of_substrings("abc") == 6  # There are 6 non-empty substrings: "a", "b", "c", "ab", "bc", "abc"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15
